
from django.shortcuts import render
#from django.views import generic
#from .models import Post

posts = [
    {
        'author': 'myusername',
        'title': 'First Blog Post',
        'content': 'First Post Content',
        'date_posted': 'June 24, 2022',
    },
    {
        'author': 'Claire Joy',
        'title': 'Second Blog Post',
        'content': 'Second Post Content',
        'date_posted': 'June 25, 2022',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})