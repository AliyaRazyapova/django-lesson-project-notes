from django.test import TestCase

from web.models import Note, User


class ExampleTestCase(TestCase):
    def test_example(self):
        note = Note.objects.create(
            title='test',
            text='test',
            user=User.objects.create(
                email='test@test.ru'
            )
        )
        self.assertIsNotNone(note.created_at)
