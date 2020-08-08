from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

from Group.forms import GroupAddForm, GroupEditForm
from Group.models import Group

# Create your views here.


def group_list(request):
    qs = Group.objects.all()

    if request.GET.get('Id'):
        qs = qs.filter(name=request.GET.get('Id'))

    if request.GET.get('course'):
        qs = qs.filter(course=request.GET.get('course'))

    if request.GET.get('email'):
        qs = qs.filter(classrooom=request.GET.get('email'))

    result = '<br>'.join(
        str(group)
        for group in qs
    )

    return render(
        request=request,
        template_name='group_list.html',
        context={'group_list': qs}
    )


def group_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            group = form.save()
            print(f'Group created:{group}')
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='group_add.html',
        context={'form': form}
    )


def group_edit(request, id):
    try:
        group = Group.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Group with id={id} doesn't exist")

    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)

        if form.is_valid():
            group = form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    else:
        form = GroupEditForm(
            instance=group
        )

    return render(
        request=request,
        template_name='group_edit.html',
        context={'form': form,
                 'title': 'Group edit',
                 'group': group
                 }
    )


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'group_list.html'
    context_object_name = 'group_list'
    login_url = reverse_lazy('account:login')

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.order_by('-id')

        if request.GET.get('Id'):
            qs = qs.filter(id=request.GET.get('Id'))

        if request.GET.get('name'):
            qs = qs.filter(name__contains=request.GET.get('name'))

        if request.GET.get('course'):
            qs = qs.filter(course__contains=request.GET.get('course'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Group list'
        return context


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    template_name = 'group_edit.html'
    form_class = GroupEditForm
    login_url = reverse_lazy('account:login')

    def get_success_url(self):
        return reverse('groups:list')


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_add.html'
    form_class = GroupAddForm
    login_url = reverse_lazy('account:login')

    def get_success_url(self):
        return reverse('groups:list')
