from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Привет джанго')

def catalog(request):
    return HttpResponse('Catalog')