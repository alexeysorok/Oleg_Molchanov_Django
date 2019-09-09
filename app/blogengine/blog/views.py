from django.shortcuts import render
from .models import *


def post_list(request):
    # n = 'Oleg'
    # list_names = ['Alex', 'Kostya', 'Yana']
    posts = Post.objects.all()  # получить все посты

    return render(request, 'blog/index.html',
                  context={'posts': posts})


def post_detail(request, slug):  # slug придет из именнованой группы символов
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html',
                  context={'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html',
                  context={'tags': tags})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html',
                  context={'tag': tag})
