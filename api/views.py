from django.db.models import Prefetch
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.serializers import NoteSerializer
from web.models import Note, NoteComment


@api_view
def status_view(request):
    return Response({
        "status": "ok"
    })


@api_view(['GET', 'POST'])
def notes_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = NoteSerializer(
            data=data,
            context={"request": request},
            initial={"user_id": request.user.id}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    notes = Note.objects.all().optimize_for_lists().prefetch_related(
        Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
    )
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view()
def note_view(request, id):
    note = get_object_or_404(Note, id=id)
    serializer = NoteSerializer(note)
    return Response(serializer.data)
