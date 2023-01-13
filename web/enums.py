from django.db import models


class Role(models.TextChoices):
    admin = "admin", "Администратор"
    staff = "staff", "Сотрудник"
    user = "user", "Пользователь"
