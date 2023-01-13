from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from web.models import Note, User


class NoteFiltersTestCase(TestCase):
    def test_list(self):
        user = User.objects.create(email='test@test.ru')
        note = Note.objects.create(title='test note title', text='test', user=user)
        self.client.force_login(user)
        response = self.client.get(reverse('notes_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, note.title)
