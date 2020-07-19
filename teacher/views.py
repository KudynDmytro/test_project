from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from teacher.forms import TeacherAddForm
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
        context={'teacher_list': result}
    )


def teacher_add(request):
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            print(f'Teacher created:{teacher}')
            return HttpResponseRedirect(reverse('teachers'))
    else:
        form = TeacherAddForm()

    return render(
        request=request,
        template_name='teacher_add.html',
        context={'form': form}
    )
