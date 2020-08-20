from django.urls import path

from account.views import CreateAccountView, SucceedRegistrationView, AccountLoginView, \
    AccountLogoutView, AccountUpdateView, user_account_update_profile, user_account_create_profile

app_name = 'acc'

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name='registration'),
    # path('register/', user_account_create_profile, name='registration'),
    path('success/', SucceedRegistrationView.as_view(), name='success'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    # path('profile/', UserAccountUpdateView.as_view(), name='profile'),
    path('profile/', user_account_update_profile, name='profile'),
]
