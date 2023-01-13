from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.db import models

from web.enums import Role


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def _create_user(self, email, password, commit=True, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, role=Role.admin, **extra_fields)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(unique=True)
    role = models.CharField(
        choices=Role.choices,
        max_length=15,
        default=Role.user
    )
    name = models.CharField(max_length=255, null=True, blank=True)

    @property
    def is_staff(self):
        return self.role in (Role.admin, Role.staff)

    @property
    def is_superuser(self):
        return self.role == Role.admin

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'


class Tag(BaseModel):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_tag = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'


class Note(BaseModel):
    title = models.CharField(max_length=500, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    alert_send_at = models.DateTimeField(null=True, blank=True, verbose_name='Время напоминания')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Теги')

    def __str__(self):
        return f'Note #{self.id} "{self.title}"'

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'


class NoteComment(BaseModel):
    note = models.ForeignKey(
        Note, on_delete=models.CASCADE, verbose_name='Заметка', related_name='comments'
    )
    text = models.TextField(verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
