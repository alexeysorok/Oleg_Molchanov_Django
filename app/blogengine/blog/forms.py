from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm): # ModelForm позволяет сделаеть класс более универсальным за счет связывания с моделью
    # title = forms.CharField(max_length=50)  # CharField соответсвуте полю input
    # slug = forms.CharField(max_length=50)

    # # переопределяем для того чтобы задействовать на отображении bootstrap
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),

        }

    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag

    # пишем для какого поля clean_slug
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create')
        if Tag.objects.Filter(slug__iexact=new_slug).count():
            raise ValidationError(
                'Slug mast be unique. We have "{}" slug already'.format(new_slug))
        return new_slug
