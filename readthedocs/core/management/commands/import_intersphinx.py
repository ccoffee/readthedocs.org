from django.core.management.base import BaseCommand

from builds.constants import LATEST
from builds.models import Version
from projects.tasks import update_intersphinx


class Command(BaseCommand):
    def handle(self, *args, **options):
        for version in Version.objects.filter(slug=LATEST):
            update_intersphinx(version.pk)
