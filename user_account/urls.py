from django.urls import path

from user_account.views import CreateUserAccountView, SucceedRegistrationView, UserAccountLoginView, \
    UserAccountLogoutView, UserAccountUpdateView, user_account_update_profile, user_account_create_profile

app_name = 'account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    # path('register/', user_account_create_profile, name='registration'),
    path('success/', SucceedRegistrationView.as_view(), name='success'),
    path('login/', UserAccountLoginView.as_view(), name='login'),
    path('logout/', UserAccountLogoutView.as_view(), name='logout'),
    # path('profile/', UserAccountUpdateView.as_view(), name='profile'),
    path('profile/', user_account_update_profile, name='profile'),
]
