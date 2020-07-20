"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import students_list, students_add, students_edit, students_delete
from teacher.views import teacher_list, teacher_add, teachers_edit
from Group.views import group_list, group_add, group_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('students/', students_list, name='students'),
    path('students/add/', students_add),
    path('students/delete/<int:id>', students_delete),
    path('students/edit/<int:id>', students_edit),
    path('teachers/', teacher_list, name='teachers'),
    path('teachers/add/', teacher_add),
    path('teachers/edit/<int:id>', teachers_edit),
    path('group/edit/<int:id>', group_edit),
    path('group/', group_list, name='groups'),
    path('group/add/', group_add),
]
