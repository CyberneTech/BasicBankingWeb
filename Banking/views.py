from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
    },
    {
        'author': 'Something else',
        'title': 'Blog Post 2',
    }
]

def home (request):
    return render(request,'home.html',{ "posts": posts })
