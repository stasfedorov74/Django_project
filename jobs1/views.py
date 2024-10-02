from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def MainJobs(request):
    return HttpResponse("Тут будет основной функционал")