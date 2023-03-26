from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})

def detail(request, id):
    return render(request, 'detail.html', {})

