from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from account.forms import AccountRegistrationForm, AccountProfileForm, ProfileUpdateForm


class CreateAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = AccountRegistrationForm

    def get_success_url(self):
        return reverse('acc:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class AccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as user'}
    # success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     return reverse('index')


class AccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout from account'}


class AccountUpdateView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = AccountProfileForm

    def get_object(self):
        return self.request.user


class SucceedRegistrationView(ListView):
    model = User
    template_name = 'success.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Registration is over'
        return context


@login_required
def user_account_update_profile(request):
    if request.method == 'POST':
        u_form = AccountProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('acc:profile')

    else:
        u_form = AccountProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': f'Edit {request.user.get_full_name()} user profile'
    }

    return render(
        request=request,
        template_name='profile.html',
        context=context
    )


def user_account_create_profile(request):
    if request.method == 'POST':
        u_form = AccountRegistrationForm(request.POST, instance=request.user)
        p_form = AccountProfileForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('acc:login')

    else:
        u_form = AccountRegistrationForm(instance=request.user)
        p_form = AccountProfileForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': f'Edit {request.user.get_full_name()} user profile'
    }

    return render(
        request=request,
        template_name='registration.html',
        context=context
    )
