from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def transfer(request):
    return HttpResponse('<h1>This is transfer<h1>')


def view(request):
    return HttpResponse('<h1>This is View of transactions<h1>')    