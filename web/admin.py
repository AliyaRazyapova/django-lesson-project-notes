from django.contrib import admin

from web.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at')
    list_display_links = ('id', 'title')


admin.site.register(Note, NoteAdmin)