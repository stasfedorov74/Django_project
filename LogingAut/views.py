from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Login(request):
    return HttpResponse("<h1>Здесь должна быть страница авторизации</h1>")