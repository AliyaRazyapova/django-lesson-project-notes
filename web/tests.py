from datetime import datetime
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from web.models import Note, User


class NoteFiltersTestCase(TestCase):
    def test_list(self):
        def setUp(self) -> None:
            self.user = User.objects.create(email='test@test.ru')
            self.note = Note.objects.create(title='test note title', text='test', user=self.user)
            self.client.force_login(self.user)

        def _check_response(self, query_params=None):
            response = self.client.get(reverse('notes_list'), data=query_params)
            self.assertEqual(response.status_code, HTTPStatus.OK)
            return response

        def test_list(self):
            response = self._check_response()
            self.assertContains(response, self.note.title)

        def test_list_with_alerts(self):
            note_with_alert = Note.objects.create(
                title='note with alert',
                text='test',
                user=self.user,
                alert_send_at=datetime.now()
            )
            response = self._check_response({"with_alerts": 1})
            self.assertNotContains(response, self.note.title)
            self.assertContains(response, note_with_alert.title)
