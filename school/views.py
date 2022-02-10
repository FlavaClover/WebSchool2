from django.shortcuts import render
from django.http import HttpResponse
from school.forms import LoginForm

def index(request):
    if request.POST:
        print('POST')
    return render(request, 'index.html', context={'LoginForm': LoginForm})


