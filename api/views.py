from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import NoteSerializer
from web.models import Note


@api_view
def status_view(request):
    return Response({
        "status": "ok"
    })


@api_view()
def notes_view(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view()
def note_view(request, id):
    note = get_object_or_404(Note, id=id)
    serializer = NoteSerializer(note)
    return Response(serializer.data)
