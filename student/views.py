from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from student.forms import StudentAddForm, StudentEditForm, StudentDeleteForm
from student.models import Student

# Create your views here.


def students_list(request):
    qs = Student.objects.all().select_related('group')

    if request.GET.get('fname'):
        qs = qs.filter(first_name__contains=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name__contains=request.GET.get('lname'))

    if request.GET.get('email'):
        qs = qs.filter(email__contains=request.GET.get('email'))

    if request.GET.get('pnum'):
        qs = qs.filter(phone_num__contains=request.GET.get('pnum'))

    result = '<br>'.join(
        str(student)
        for student in qs
    )

    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': qs,
                 'title': 'Student list'
                 }
    )


def students_add(request):
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            student = form.save()
            n = Student.objects.filter(phone_num=student.phone_num)
            e = Student.objects.filter(email=student.email)
            if n:
                return HttpResponse('Student with such phone number already exists')
            elif e:
                return HttpResponse('Student with such email already exists')
            print(student)
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentAddForm()

    return render(
        request=request,
        template_name='students_add.html',
        context={'form': form,
                 'title': 'Student add'
                 }
    )


def students_edit(request, id):
    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_edit.html',
        context={'form': form,
                 'title': 'Student edit'
                 }
    )


def students_delete(request, id):

    try:
        student = Student.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Student with id={id} doesn't exist")

    if request.method == 'POST':
        form = StudentDeleteForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save()
            student.delete()
            return HttpResponseRedirect(reverse('students:list'))
    else:
        form = StudentEditForm(
            instance=student
        )

    return render(
        request=request,
        template_name='students_delete.html',
        context={'form': form,
                 'title': 'Are you sure, you want to delete this student?'
                 }
    )


class StudentsListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        request = self.request
        qs = super().get_queryset()
        qs = qs.select_related('group').order_by('-id')

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
        context['title'] = 'Student list'
        return context


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students_edit.html'
    form_class = StudentEditForm

    def get_success_url(self):
        return reverse('students:list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit student'
        return context


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students_add.html'
    form_class = StudentAddForm

    def get_success_url(self):
        return reverse('students:list')


class StudentsDeleteView(DeleteView):
    model = Student
    template_name = 'students_delete.html'
    form_class = StudentDeleteForm

    def get_success_url(self):
        return reverse('students:list')
