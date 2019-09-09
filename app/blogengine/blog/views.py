from django.shortcuts import render

# Create your views here.
def post_list(request):
    n = 'Oleg'
    list_names = ['Alex', 'Kostya', 'Yana']
    return render(request, 'blog/index.html', 
        context={'names': list_names}) # name - будет использоваться в шаблоне