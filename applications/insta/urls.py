from django.urls import path
from .views import (
    index, get_all_posts, get_details
)

urlpatterns = [
    path('', index, ),
    path('posts/', get_all_posts, name='posts'),
    path('posts/<int:id>/', get_details, name='post_detail'),

    #http://localhost:8000/posts/
    #http://localhost:8000/posts/1/
]

