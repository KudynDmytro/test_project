from django.urls import path

from teacher.views import teacher_list, teacher_add, teachers_edit, TeacherListView, TeacherCreateView, \
    TeacherUpdateView

app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='list'),
    path('add/', TeacherCreateView.as_view(), name='add'),
    path('edit/<int:pk>', TeacherUpdateView.as_view(), name='edit'),
]
