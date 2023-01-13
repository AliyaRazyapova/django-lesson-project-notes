import factory

from web.models import Note, User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("email")

    class Meta:
        model = User


class NoteFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("word")
    text = factory.Faker("text")
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Note
