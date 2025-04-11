from django.shortcuts import render, get_object_or_404
from .models import Post



def home(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'home/home.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})