from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="MerenderoAdmin").exists():
            User.objects.create_superuser("MerenderoAdmin", "merendero@gmail.com", "Carrera1aw#3622")
