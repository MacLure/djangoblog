from django.shortcuts import render
from .models import Post
posts = [
    {'author': 'author1',
     'title': 'title1',
     'content': 'body1',
     'date_posted': 'date'},
    {'author': 'author2',
     'title': 'title2',
     'content': 'body2',
     'date_posted': 'date2'}, ]


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
