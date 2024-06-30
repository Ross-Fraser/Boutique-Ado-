from django.test import TestCase
from django.urls import path
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("index")

urlpatterns = [
    path('', test_view, name='home'),
]
