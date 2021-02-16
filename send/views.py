from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction, Users


# Create your views here.
def transfer(request):
    return render(request, 'userlist.html')


def view(request):
    return render(request, 'allrecords.html')   