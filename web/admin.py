from django.contrib import admin

from web.models import Note, Tag


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'get_text_count', 'created_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('created_at',)
    ordering = ('created_at',)
    readonly_fields = ('alert_send_at', 'get_text_count')

    # exclude = ('tags',)

    @admin.display(description='Text count')
    def get_text_count(self, instance):
        return len(instance.text)


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag)
