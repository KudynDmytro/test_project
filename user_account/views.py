from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm, UserProfileUpdateForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        return reverse('account:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title': 'Login as user'}
    # success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     return reverse('index')


class UserAccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title': 'Logout from LMS'}


class UserAccountUpdateView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = UserAccountProfileForm

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
        u_form = UserAccountProfileForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account:profile')

    else:
        u_form = UserAccountProfileForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

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
        u_form = UserAccountRegistrationForm(request.POST, instance=request.user)
        p_form = UserAccountProfileForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('account:login')

    else:
        u_form = UserAccountRegistrationForm(instance=request.user)
        p_form = UserAccountProfileForm(instance=request.user.profile)

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
