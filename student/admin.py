from django.contrib import admin

# Register your models here.
from student.models import Student


class StudentAdminModel(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'group')
    list_display = ('first_name', 'last_name', 'email', 'group')


admin.site.register(Student, StudentAdminModel)

