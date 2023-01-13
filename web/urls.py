"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import RedirectView

from web.views import login_view, logout_view,\
    RegistrationView, NotesListView, NoteDetailView, NoteCreateFormView, NoteUpdateView, NoteDeleteView, html_view,\
    stat_view

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='notes_list'), name='main'),
    path("registration/", RegistrationView.as_view(), name='registration'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("stat/", stat_view, name='stat'),
    path("notes/", NotesListView.as_view(), name="notes_list"),
    path("notes/add/", NoteCreateFormView.as_view(), name="notes_add"),
    path("notes/<str:title>/<int:id>/edit/", NoteUpdateView.as_view(), name="note_edit"),
    path("notes/<str:title>/<int:id>/delete/", NoteDeleteView.as_view(), name="note_delete"),
    path("notes/<str:title>/<int:id>/", NoteDetailView.as_view(), name="note"),
    path("html/", html_view)
]