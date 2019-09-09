from django.db import models
from django.shortcuts import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):  # метод необходим для упрощения работы с url (https://www.youtube.com/watch?v=4O1xdboP0PY&list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX&index=5)
        return reverse("post_detail_url", kwargs={"slug": self.slug})
        # первый аргумент название url шаблона
        # post_detail_url - это название name='' в urls.py


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse("tag_detail_url", kwargs={"slug": self.slug})
    
