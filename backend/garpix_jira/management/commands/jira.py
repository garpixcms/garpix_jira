from django.core.management.base import BaseCommand
import time
from ...models.server import Server


class Command(BaseCommand):
    help = 'Jira commands'

    def add_arguments(self, parser):
        parser.add_argument('command', type=str)

    def handle(self, *args, **kwargs):
        command = kwargs['command']
        if command == 'sync':
            Server.sync_all()
            time.sleep(1200)
