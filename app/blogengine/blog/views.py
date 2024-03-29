from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.views.generic import View

from .utils import *
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q



def post_list(request):
    # n = 'Oleg'
    # list_names = ['Alex', 'Kostya', 'Yana']
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) |  Q(body__icontains=search_query ))    
    else:
        posts = Post.objects.all()

    posts = Post.objects.all()  # получить все посты
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    


    return render(request, 'blog/index.html',
                  context={'page_object': page})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html',
                  context={'tags': tags})

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create.html',
    #                   context={'form': form})

    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html',
    #                   context={'form': bound_form})



# Post.mro() - покажет очереность поиска аотрибутов, важно в порядке использования наследования в классе
class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'
    # def get(self, request, slug):
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug )
    #     return render(request, 'blog/post_detail.html',
    #                   context={'post': post})

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True




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


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html',
    #                   context={'form': form})

    # def post(self, request):
    #     bound_form = TagForm(request.POST)

    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html',
    #                   context={'form': bound_form})
     model_form = TagForm
     template = 'blog/tag_create.html'
     raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):

    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True

    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update_form.html',
    #     context={'form':bound_form, 'tag': tag})

    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)

    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update_form.html',
    #     context={'form':bound_form, 'tag': tag})


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'blog/tag_delete_form.html', 
    #         context={'tag': tag})

    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_list_url'))







