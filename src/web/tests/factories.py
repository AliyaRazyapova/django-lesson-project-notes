import factory

from src.web.models import Note, User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class NoteFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("sentence")
    text = factory.Faker("text")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Note
