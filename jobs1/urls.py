from django.urls import path
from jobs1.views import MainJobs

urlpatterns = [
    path('MainJobs/', MainJobs),
]
