from django.db import models

# Create your models here.
import datetime
from django.db import models


class Group(models.Model):
    group_id = models.IntegerField(null=False)
    course = models.CharField(max_length=50, null=False)
    group_email = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.group_id}, {self.course} {self.group_email}'


