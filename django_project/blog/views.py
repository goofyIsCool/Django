from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Jan Son Ha',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'August 19, 2020'
    },
    {
        'author': 'Maciek',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'August 19, 2020'
    }
]

# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
