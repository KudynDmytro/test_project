from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Group.forms import GroupAddForm
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


def group_add(request):
    if request.method == 'POST':
        form = GroupAddForm(request.POST)
        if form.is_valid():
            group = form.save()
            print(f'Group created:{group}')
            return HttpResponseRedirect(reverse('groups'))
    else:
        form = GroupAddForm()

    return render(
        request=request,
        template_name='group_add.html',
        context={'form': form}
    )
