from django.core.management.base import BaseCommand, CommandError

from Group.models import Group
from teacher.models import Teacher


class Command(BaseCommand):
    help = 'Generate N fake teachers'

    def add_arguments(self, parser):
        parser.add_argument('num_teachers', default=100, type=int)

    def handle(self, *args, **kwargs):
        num_teachers = kwargs['num_teachers']

        Teacher.objects.all().delete()
        groups = list(Group.objects.all())

        for _ in range(num_teachers):
            Teacher.gen_teacher(groups)

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_teachers}'))
