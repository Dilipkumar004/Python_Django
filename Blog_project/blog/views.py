from django.shortcuts import render,redirect 
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html',{'posts': posts})

def post_details(request,post_id):
    post = BlogPost.objects.get(id=post_id)
    return render (request, 'blog/post_details.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html',{'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = BlogPost(title=title, content=content,author=request.user)
        post.save()
        return redirect('home')
    return render(request, 'blog/add_post.html')
