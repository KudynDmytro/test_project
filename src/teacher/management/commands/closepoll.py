from django.core.management.base import BaseCommand, CommandError, no_translations
from polls.models import Question as Poll

from src.teacher.models import Teacher


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def generate_students(self, n):
        for _ in range(n):
            Teacher.generate_student()


