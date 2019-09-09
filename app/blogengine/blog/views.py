from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import View

from .utils import ObjectDetailMixin


def post_list(request):
    # n = 'Oleg'
    # list_names = ['Alex', 'Kostya', 'Yana']
    posts = Post.objects.all()  # получить все посты

    return render(request, 'blog/index.html',
                  context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html',
                  context={'tags': tags})


class PostDetail(ObjectDetailMixin, View): # Post.mro() - покажет очереность поиска аотрибутов, важно в порядке использования наследования в классе
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug )
    #     return render(request, 'blog/post_detail.html',
    #                   context={'post': post})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Post, slug__iexact=slug )
    #     return render(request, 'blog/tag_detail.html',
    #                   context={'tag': tag})

# миксины спец классы - от них наследуется часть логики

# def post_detail(request, slug):  # slug придет из именнованой группы символов
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html',
#                   context={'post': post})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html',
#                   context={'tag': tag})
