from django.shortcuts import render

# Create your views here.
def post_list(request):
    n = 'Oleg'
    return render(request, 'blog/index.html', 
        context={'name': n}) # name - будет использоваться в шаблоне