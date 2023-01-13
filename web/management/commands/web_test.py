from django.core.management.base import BaseCommand

from web.enums import Role
from web.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user, is_created = User.objects.get_or_create(
            email='user@test.com',
            defaults={'role': Role.staff}
        )
        print(user, is_created)

        user, is_updated = User.objects.update_or_create(
            email='user@test.com',
            defaults={'role': Role.staff}
        )
        print(user, is_updated)
