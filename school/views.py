from django.shortcuts import render
from django.http import HttpResponse
from school.forms import LoginForm

def view_login(request):
    if request.POST:
        print('POST')
    return render(request, 'index.html', context={'LoginForm': LoginForm})

