from django.urls import path
from tmp1.views import helpNew
urlpatterns = [
    path('help/', helpNew),
]
