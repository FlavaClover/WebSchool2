from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from school.forms import LoginForm
from school.models import Student


def view_login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['login'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return redirect('/account/')
            else:
                return render(request, 'index.html', context={'LoginForm': LoginForm, 'msg': 'Введенны неправильные данные'})

    return render(request, 'index.html', context={'LoginForm': LoginForm})


@login_required(login_url='index')
def view_account(request):
    student = Student.objects.get(user=request.user)
    return HttpResponse(student.full_name)


@login_required(login_url='index')
def view_logout(request):
    logout(request)
    return redirect('index')

