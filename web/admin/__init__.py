from django.contrib import admin

from web.admin.note import NoteAdmin
from web.admin.tag import TagAdmin
from web.admin.user import UserAdmin
from web.models import Note, Tag, User


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)

