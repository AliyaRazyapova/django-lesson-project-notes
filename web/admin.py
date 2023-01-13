from django.contrib import admin, messages

from web.models import Note, Tag, NoteComment


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


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'get_text_count', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('alert_send_at', 'get_text_count')
    # exclude = ('tags',)
    actions = (set_title_to_uppercase,)
    inlines = (NoteCommentInline,)
    @admin.display(description='Text count')
    def get_text_count(self, instance):
        return len(instance.text)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

    def has_delete_permission(self, request, obj=None):
        if obj is None:
            return False
        return request.user == obj.user

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(NoteComment)
