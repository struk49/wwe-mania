from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()  # Retrieve all posts from the database
    return render(request, 'home/home.html', {'posts': posts})