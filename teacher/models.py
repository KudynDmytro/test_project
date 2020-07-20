import datetime

from django.db import models

# Create your models here.
from faker import Faker

from Group.models import Group


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True)
    birthdate = models.DateField(default=datetime.date.today())
    phone_num = models.CharField(max_length=40, null=True)
    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.birthdate}'

    @classmethod
    def gen_teacher(cls):
        faker = Faker()

        teacher = Teacher(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_num=faker.phone_number()
        )

        teacher.save()


