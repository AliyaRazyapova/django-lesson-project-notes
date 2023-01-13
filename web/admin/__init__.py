from django.contrib import admin

from web.admin.note import NoteAdmin
from web.admin.tag import TagAdmin
from web.models import Note, Tag


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
