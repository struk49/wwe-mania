from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import PostForm
from .decorators import superuser_required  # use your custom decorator
from .models import Post



def home(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'home/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})


@login_required
@superuser_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'home/add_post.html', {'form': form})

@login_required
@superuser_required
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')