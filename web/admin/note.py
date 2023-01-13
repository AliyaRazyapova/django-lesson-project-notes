from django.contrib import admin, messages
from web.db_utils import SplitPartFunc
from web.models import Note, NoteComment, User
from web.models import Note, Tag, NoteComment, User


@admin.display(description='Привести название к верхнему регистру')
def set_title_to_uppercase(modeladmin, request, queryset):
    objects = []
    for item in queryset:
        item.title = item.title.upper()
        objects.append(item)
    Note.objects.bulk_update(objects, ['title'])
    messages.add_message(
        request,
        messages.SUCCESS,
        f'Обновлены {len(objects)} объектов'
    )


class NoteCommentInline(admin.TabularInline):
    model = NoteComment


class AuthorEmailDomainFilter(admin.SimpleListFilter):
    title = 'Домен автора заметки'
    parameter_name = 'author_email_domain'

    def has_output(self):
        return True

    def lookups(self, request, model_admin):
        email_domains = (
            User.objects.all()
            .annotate(email_domain=SplitPartFunc("email", "@", 2))
            .distinct()
            .values_list("email_domain", flat=True)
        )
        return ((d, d) for d in email_domains)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__email__endswith=f'@{self.value()}')
        return queryset


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'get_text_count', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('created_at', 'tags', AuthorEmailDomainFilter)
    ordering = ('created_at',)
    readonly_fields = ('get_text_count',)
    # exclude = ('tags',)
    actions = (set_title_to_uppercase,)
    inlines = (NoteCommentInline,)

    @admin.display(description='Text count')
    def get_text_count(self, instance):
        return len(instance.text)
