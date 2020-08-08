from django.urls import path

from user_account.views import CreateUserAccountView, SucceedRegistrationView

app_name = 'account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('success/', SucceedRegistrationView.as_view(), name='success'),
]
