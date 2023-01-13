import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from src.web.tests.factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


def test_status(api_client):
    response = api_client.get(reverse("status"))
    assert response.status_code == status.HTTP_200_OK


def test_notes(api_client, note):
    api_client.force_login(note.user)
    response = api_client.get(reverse("notes-list"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


def test_note(api_client, note):
    api_client.force_login(note.user)
    response = api_client.get(reverse("notes-detail", args=(note.id,)))
    assert response.status_code == status.HTTP_200_OK
    assert note.id == response.json()['id']


def test_note_create(api_client, user):
    api_client.force_login(user)
    response = api_client.post(
        reverse("notes-list"),
        data={"title": "test", "text": "test"}
    )
    assert response.status_code == status.HTTP_201_CREATED, response.content


def test_note_update(api_client, note):
    api_client.force_login(note.user)
    UserFactory()
    response = api_client.put(
        reverse("notes-detail", args=(note.id,)),
        data={"title": "new_title", "text": "test"}
    )
    assert response.status_code == status.HTTP_200_OK, response.content
    note.refresh_from_db()
    assert note.title == "new_title"
