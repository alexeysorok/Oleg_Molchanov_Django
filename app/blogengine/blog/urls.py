from django.urls import path

from .views import *

urlpatterns = [
    path('', post_list, name='posts_list_url'),
    path('post/<str:slug>/',post_detail, name='post_detail_url'), # угловые скобки означают именованные группы символов, нужно присвоить ей имя
    path('tags/', tags_list, name='tags_list_url'),
]

