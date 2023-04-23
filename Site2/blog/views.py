from django.shortcuts import render, redirect, View
from blog.models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
     posts = Post.objects.all()
     paginator = Paginator(posts, 3)
     page = request.GET.get('page')
     return render(request, 'index.html', {"posts": posts})
def detail(request, pk):
     post = Post.objects.get(id=pk)
     return render(request, 'detail.html', {"post": post})

def view_Login(request):
     if request.method =='POST':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
               username = form.cleaned_data('username')
               password = form.cleaned_data('password')
               user = authenticate(username = username, password = password)
               if user is not None:
                    login(request, user)
                    return redirect('home')

def logout_view(request):
     logout(request)
     return redirect(login)

class Register(View):
     form_class = UserCreationForm
     template_name = 'register,html'

     def get(self, request):
          form = self.form_class()
          return render(request, self.template_name, {'form': form})

     def post(self, request):
          form = self.form_class(request.POST)
          if form.is_valid():
               user = form.save()
               return redirect('login')
          return render(request, self.template_name, {'form': form})