from django.http import HttpResponse
from django.shortcuts import render

from web.models import Note


def main_view(request):
    notes = Note.objects.all()
    for note in notes:
        print(note.title)
        print(note.text)
        print(note.user)
        print(note.user.first_name)
    return render(request, 'web/main.html')
