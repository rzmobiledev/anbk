from django.core.management import BaseCommand
import time
from psycopg2 import OperationalError as PgError
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django commit to database"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        wakeup = False

        while not wakeup:
            try:
                self.check(databases=["default"])
                wakeup = True

            except (PgError, OperationalError):
                self.stdout.write("Waiting for 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("YOUR DATABASE IS READY!"))
