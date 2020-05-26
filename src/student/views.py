from django.shortcuts import render
from django.http import HttpResponse
from student.models import Student

# Create your views here.


def students_list(request):
    qs = Student.objects.all()

    if request.GET.get('fname'):
        qs = qs.filter(first_name__contains=request.GET.get('fname'))

    if request.GET.get('lname'):
        qs = qs.filter(last_name__contains=request.GET.get('lname'))

    if request.GET.get('email'):
        qs = qs.filter(email__contains=request.GET.get('email'))

    # if request.GET.get()

    result = '<br>'.join(
        str(student)
        for student in qs
    )

    # return HttpResponse(result)
    return render(
        request=request,
        template_name='students_list.html',
        context={'students_list': result}
    )
