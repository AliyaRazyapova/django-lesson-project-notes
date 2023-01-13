from django.db.models import Prefetch
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import NoteSerializer
from web.models import Note, NoteComment


@api_view
def status_view(request):
    return Response({
        "status": "ok"
    })


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all().optimize_for_lists().prefetch_related(
        Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
    )
    serializer_class = NoteSerializer
