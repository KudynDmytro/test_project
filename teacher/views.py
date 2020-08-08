from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView

from teacher.forms import TeacherAddForm, TeacherEditForm
from teacher.models import Teacher

# Create your views here.


def teacher_list(request):
    qs = Teacher.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name=request.GET.get('lname'))

    if request.GET.get('email'):
        qs = qs.filter(email=request.GET.get('email'))

    if request.GET.get('pnum'):
        qs = qs.filter(phone_num__contains=request.GET.get('pnum'))

    result = '<br>'.join(
        str(teacher)
        for teacher in qs
    )

    return render(
        request=request,
        template_name='teacher_list.html',
        context={'teacher_list': qs,
                 'title': 'Teacher list'}
    )


def teacher_add(request):
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            print(f'Teacher created:{teacher}')
            return HttpResponseRedirect(reverse('teachers:list'))
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teacher_add.html',
        context={'form': form,
                 'title': 'Teacher add'
                 }
    )


def teachers_edit(request, id):

    try:
        teacher = Teacher.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Teacher with id={id} doesn't exist")

    if request.method == 'POST':
        form = TeacherAddForm(request.POST, instance=teacher)

        if form.is_valid():
            teacher = form.save()
            print(f'Student created:{teacher}')
            return HttpResponseRedirect(reverse('teachers:list'))
    else:
        form = TeacherEditForm(
            instance=teacher
        )

    return render(
        request=request,
        template_name='teacher_edit.html',
        context={'form': form,
                 'title': 'Teacher edit'
                 }
    )


class TeacherListView(LoginRequiredMixin, ListView):
    model = Teacher
    template_name = 'teacher_list.html'
    context_object_name = 'teacher_list'
    login_url = reverse_lazy('account:login')

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group')
        qs = qs.order_by('-id')

        if request.GET.get('fname'):
            qs = qs.filter(first_name__contains=request.GET.get('fname'))

        if request.GET.get('lname'):
            qs = qs.filter(last_name__contains=request.GET.get('lname'))

        if request.GET.get('email'):
            qs = qs.filter(email__contains=request.GET.get('email'))

        if request.GET.get('pnum'):
            qs = qs.filter(phone_num__contains=request.GET.get('pnum'))

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Teacher list'
        return context


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    template_name = 'teacher_edit.html'
    form_class = TeacherEditForm
    login_url = reverse_lazy('account:login')

    def get_success_url(self):
        return reverse('teachers:list')


class TeacherCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    template_name = 'teacher_add.html'
    form_class = TeacherAddForm
    login_url = reverse_lazy('account:login')

    def get_success_url(self):
        return reverse('teachers:list')

