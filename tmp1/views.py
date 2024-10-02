from django.http import HttpResponse

# Create your views here.
def helpNew (request):
    return HttpResponse("<h1>Help</h1>")