from django.http import HttpResponse
from django.shortcuts import render

from web.models import Note


def main_view(request):
    with_alerts = 'with_alerts' in request.GET
    search = request.GET.get('search', None)
    notes = Note.objects.all()

    if with_alerts:
        notes = notes.filter(alert_send_at__isnull=False)

    if search:
        # SELECT * FROM web_note WHERE title = "..."
        notes = notes.filter(title=search)

    return render(request, "web/main.html", {
        'count': Note.objects.count(),
        'notes': notes,
        'with_alerts': with_alerts,
        'query_params': request.GET,
        'search': search
    })
