from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from web.forms import NoteForm, AuthForm
from web.models import Note, Tag, User


def main_view(request):
    return redirect("notes_list")


def notes_view(request):
    with_alerts = 'with_alerts' in request.GET
    search = request.GET.get('search', None)
    try:
        tag_id = int(request.GET.get("tag_id", None))
    except (TypeError, ValueError):
        tag_id = None

    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user).order_by('-created_at')
    else:
        notes = Note.objects.none()

    if with_alerts:
        notes = notes.filter(alert_send_at__isnull=False)

    if search:
        notes = notes.filter(
            Q(title__icontains=search) |
            Q(text__icontains=search)
        )

    if tag_id:
        tag = Tag.objects.get(id=tag_id)
        notes = notes.filter(tags__in=[tag])

    return render(request, "web/main.html", {
        'count': Note.objects.count(),
        'notes': notes,
        'with_alerts': with_alerts,
        'query_params': request.GET,
        'search': search,
        'tags': Tag.objects.all(),
        'tag_id': tag_id,
    })


@login_required()
def note_view(request, id):
    note = get_object_or_404(Note, user=request.user, id=id)
    return render(request, "web/note.html", {
        'note': note
    })


@login_required
def note_edit_view(request, id=None):
    form = NoteForm()

    if id is not None:
        note = get_object_or_404(Note, user=request.user, id=id)
        form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, initial={'user': request.user})
        if form.is_valid():
            note = note.save()
            return redirect('note', note.id)
    return render(request, "web/note_form.html", {
        'id': id,
        'form': form
    })


def registration_view(request):
    form = AuthForm()
    is_success = False
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User(username=username)
            user.set_password(form.cleaned_data['password'])
            user.save()
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        'is_success': is_success
    })


def login_view(request):
    form = AuthForm()
    message = None
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is None:
                message = "Электронная почта или пароль неправильные"
            else:
                login(request, user)
                next_url = 'main'
                if 'next' in request.GET:
                    next_url = request.GET.get("next")
                return redirect(next_url)
    return render(request, "web/login.html", {
        "form": form,
        'message': message
    })


def logout_view(request):
    logout(request)
    return redirect('main')
