from django.urls import path

from Group.views import group_list, group_add, group_edit, GroupListView, GroupUpdateView, GroupCreateView

app_name = 'groups'

urlpatterns = [
    path('edit/<int:pk>', GroupUpdateView.as_view(), name='edit'),
    # path('edit/<int:id>', group_edit, name='edit'),
    path('', GroupListView.as_view(), name='list'),
    # path('', group_list, name='list'),
    path('add/', GroupCreateView.as_view(), name='add'),
    # path('add/', group_add, name='add'),
]
