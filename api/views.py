from django.db.models import Prefetch
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import NoteSerializer
from web.models import Note, NoteComment


@api_view
def status_view(request):
    return Response({
        "status": "ok"
    })


class NoteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Note.objects.all().optimize_for_lists().prefetch_related(
        Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
    )
    serializer_class = NoteSerializer


@api_view(['GET', 'PUT'])
def note_view(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "PUT":
        serializer = NoteSerializer(
            instance=note,
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = NoteSerializer(note)
    return Response(serializer.data)
