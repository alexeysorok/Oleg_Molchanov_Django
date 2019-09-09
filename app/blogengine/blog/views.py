from django.shortcuts import render
from .models import *

# Create your views here.
def post_list(request):
    # n = 'Oleg'
    # list_names = ['Alex', 'Kostya', 'Yana']
    posts = Post.objects.all() # получить все посты

    return render(request, 'blog/index.html', 
        context={'posts': posts}) 

def post_detail(request, slug): # slug придет из именнованой группы символов
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', 
            context={'post': post})