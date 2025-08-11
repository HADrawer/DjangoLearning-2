from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return render(request, 'hello.html', {
        'name' : 'ibrahim',
        'categories' : [
            'Catagory 1',
            'Catagory 1',
            'Catagory 2',
            'Catagory 3',
            'Catagory 4',
        ]
    })


def show_article(request , id, slug):
    return render(request, 'article/show_article.html', {
        'title' : 'Article ' + str(id),
        'content': 'Article content ' + str(slug)
    })


def home(request):
    return render(request , 'home.html')

def about(request):
     return render(request, "about.html")