from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, post_detail , add_post # <- this imports the view functions

urlpatterns = [
    path('', home, name='home'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/add/', add_post, name='add_post'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]