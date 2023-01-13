from django.contrib import admin

from src.web.admin.note import NoteAdmin
from src.web.admin.tag import TagAdmin
from src.web.admin.user import UserAdmin
from src.web.models import Note, Tag, User


admin.site.register(Note, NoteAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(User, UserAdmin)

