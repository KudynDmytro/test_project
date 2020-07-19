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
from student.views import students_list, students_add
from teacher.views import teacher_list, teacher_add
from Group.views import group_list, group_add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('students/', students_list, name='students'),
    path('students/add/', students_add),
    path('teacher/', teacher_list, name='teachers'),
    path('teacher/add/', teacher_add),
    path('group/', group_list, name='groups'),
    path('group/add/', group_add),
]
