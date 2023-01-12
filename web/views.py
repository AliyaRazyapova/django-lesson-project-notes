from django.http import HttpResponse
from django.shortcuts import render

from web.models import Note


def main_view(request):
    notes = Note.objects.all()

    return render(request, "web/main.html", {
        'count': Note.objects.count(),
        'example_list': [
            {"name": "Вася", "age": None},
            {"name": "Петя", "age": 22},
        ],
        'a': True,
        "b": "test"
    })
