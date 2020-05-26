import datetime

from django.db import models

# Create your models here.
from faker import Faker
from student.models import Student


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=True)
    birthdate = models.DateField(default=datetime.datetime.now().date())

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.birthdate}'

    @classmethod
    def gen_teacher(cls):
        faker = Faker()

        teacher = Teacher(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
        )

        teacher.save()

    # @classmethod
    # def generate_student(cls):
    #     faker = Faker()
    #
    #     student = Student(
    #         first_name=faker.first_name(),
    #         last_name=faker.last_name(),
    #         email=faker.email(),
    #     )
    #
    #     student.save()
