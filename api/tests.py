import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from web.tests.factories import UserFactory


@pytest.fixture
def api_client():
    return APIClient()


def test_status(api_client):
    response = api_client.get(reverse("status"))
    assert response.status_code == status.HTTP_200_OK


def test_notes(api_client, note):
    response = api_client.get(reverse("notes"))
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) > 0


def test_note(api_client, note):
    response = api_client.get(reverse("note", args=(note.id,)))
    assert response.status_code == status.HTTP_200_OK
    assert note.id == response.json()['id']


def test_note_create(api_client):
    UserFactory()
    response = api_client.post(
        reverse("notes"),
        data={"title": "test", "text": "test"}
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_note_update(api_client, note):
    UserFactory()
    response = api_client.put(
        reverse("note", args=(note.id,)),
        data={"title": "new_title", "text": "test"}
    )
    assert response.status_code == status.HTTP_200_OK
    note.refresh_from_db()
    assert note.title == "new_title"