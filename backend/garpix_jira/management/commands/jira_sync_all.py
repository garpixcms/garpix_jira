from django.core.management.base import BaseCommand
import time
from ...models.server import Server


class Command(BaseCommand):
    help = 'Jira sync all data'

    def handle(self, *args, **kwargs):
        while True:
            Server.sync_all()
            time.sleep(1200)
