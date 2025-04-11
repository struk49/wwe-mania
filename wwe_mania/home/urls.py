from django.urls import path
from .views import home, post_detail  # <- this imports the view functions

urlpatterns = [
    path('', home, name='home'),
    path('posts/<int:pk>/', post_detail, name='post_detail')
]