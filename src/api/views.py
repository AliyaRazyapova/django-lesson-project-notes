from django.db.models import Prefetch
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.api.serializers import NoteSerializer
from src.web.models import Note, NoteComment


@api_view
@permission_classes([])
def status_view(request):
    return Response({
        "status": "ok", "user_id": request.user.id
    })


class NoteViewSet(ModelViewSet):
    def get_serializer(self, *args, **kwargs):
        return NoteSerializer(*args, **kwargs, context={
            "request": self.request
        })

    def get_queryset(self):
        return Note.objects.all().optimize_for_lists().prefetch_related(
            Prefetch('comments', NoteComment.objects.all().order_by("created_at"))
        ).filter(user=self.request.user)
