from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from rest_framework.authtoken.models import Token

from colors.models import ColorBox


class Command(BaseCommand):
    help = "Bootstrap app"

    def handle(self, *args, **options):
        for user_id in range(1, 3):
            user = get_user_model().objects.create(username=f"user{user_id}")
            user.set_password(f"user{user_id}")
            user.save()
            Token.objects.get_or_create(user=user)
            for colorbox_id in range(1, 11):
                ColorBox.objects.create(user=user, color="000000")
