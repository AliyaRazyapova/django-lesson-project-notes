from django.http import HttpResponse
from django.shortcuts import render

from web.models import Note


def main_view(request):
    notes = Note.objects.all()

    for note in notes:
        print(note)
        print(note.title)
        print(note.text)
        print(note.user)
        print(note.user.first_name)

        # SELECT auth_user.id FROM web_note
        # INNER JOIN auth_user ON web_note.user_id = auth_user.id
        print(note.user.id)

        # SELECT user_id FROM web_note
        print(note.user_id)


    return render(request, 'web/main.html')
