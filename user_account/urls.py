from django.urls import path

from user_account.views import CreateUserAccountView, SucceedRegistrationView, UserAccountLoginView, \
    UserAccountLogoutView, UserAccountProfileView

app_name = 'account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('success/', SucceedRegistrationView.as_view(), name='success'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    path('profile/', UserAccountProfileView.as_view(), name='profile'),
]
