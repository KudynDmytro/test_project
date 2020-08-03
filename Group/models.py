from django.db import models

# Create your models here.
import datetime
from django.db import models
from faker.generator import random


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(max_length=128, null=True)

    def __str__(self):
        return f'{self.name} - Floor# {self.floor}'

    @classmethod
    def generate_classroom(cls):
        classroom = cls(
            name=f'Classroom - {random.choice(range(5))}',
            floor=random.choice(range(5))
            )

        classroom.save()


class Group(models.Model):
    name = models.CharField(max_length=64, null=True)
    course = models.CharField(max_length=128, null=True)
    classroom = models.ManyToManyField(
        to=Classroom,
        null=True,
        related_name='groups'
    )

    def __str__(self):
        return f'{self.name}, {self.course}'

    @classmethod
    def generate_group(cls):
        group = cls(
            name=f'Group - {random.choice(range(5))}',
            course=random.choice([
                'Network Specialist. E-Learning.',
                'Web Dev - E-Learning. E-Learning.',
                'Infrastructure Technician. E-Learning.',
                'Security Technologist. E-Learning.',
                'Software Developer - E-Learning. E-Learning.'
            ])
        )

        group.save()

