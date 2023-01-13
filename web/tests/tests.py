from datetime import datetime
from http import HTTPStatus
from random import randint

import pytest
from django.urls import reverse

from web.tests.factories import NoteFactory


def test_unauthorized(client):
    response = client.get(reverse("notes_list"))
    registration_link = reverse('registration')
    assert registration_link in response.content.decode()


@pytest.fixture
def note_with_login(client, note):
    client.force_login(note.user)
    return note


def check_response(client, query_params=None):
    response = client.get(reverse('notes_list'), data=query_params)
    assert response.status_code == HTTPStatus.OK
    return response


@pytest.mark.simple_list
def test_list(client, note_with_login):
    response = check_response(client)
    assert note_with_login.title in response.content.decode()


def test_list_with_alerts(client, note_with_login):
    note_with_alert = NoteFactory(
        user=note_with_login.user, alert_send_at=datetime.now()
    )
    response = check_response(client, {"with_alerts": 1})
    assert note_with_login.title not in response.content.decode(), 'note without alert still in response'
    assert note_with_alert.title in response.content.decode(), "note with alert isn't in response"


def test_list_with_search(client, note_with_login):
    response = check_response(client, {"search": note_with_login.title})
    assert note_with_login.title in response.content.decode()


def test_list_with_search_empty(client, note_with_login):
    response = check_response(client, {"search": str(randint(10000, 99999))})
    assert note_with_login.title not in response.content.decode()
