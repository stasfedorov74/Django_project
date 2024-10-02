from django.urls import path
from LogingAut.views import Login

urlpatterns = [
    path('login/',Login),
]