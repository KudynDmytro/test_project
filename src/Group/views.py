from django.shortcuts import render
from Group.models import Group

# Create your views here.


def group_list(request):
    qs = Group.objects.all()

    if request.GET.get('Id'):
        qs = qs.filter(first_name=request.GET.get('Id'))

    if request.GET.get('course'):
        qs = qs.filter(last_name=request.GET.get('course'))

    if request.GET.get('email'):
        qs = qs.filter(email=request.GET.get('email'))

    result = '<br>'.join(
        str(group)
        for group in qs
    )

    return render(
        request=request,
        template_name='group_list.html',
        context={'group_list': result}
    )
