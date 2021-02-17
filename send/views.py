from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction, Users


# Create your views here.
def transfer(request):
    t = Users.objects.all()
    return render(request, 'send/first.html', {'user':t})


def view(request):
    return render(request, 'send/allrecords.html')   