from django.shortcuts import render

posts = [
    {'author': 'author1',
     'title': 'title1',
     'body': 'body1',
     'date': 'asdfa'},
    {'author': 'author2',
     'title': 'title2',
     'body': 'body2',
     'date': 'asdfa'}, ]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
