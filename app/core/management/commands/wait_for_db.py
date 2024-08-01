"""djagno command to wait a database is avaliable"""
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as psycopg2Error
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """django command to wait for database to be avaliable"""
    def handle(self, *args, **options):
        """entrypoint for command"""
        self.stdout.write('Waiting for database to be avaliable')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR('Database does not exist, waiting 1 second...'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database avaliable'))
