from django.shortcuts import render
from .models import InstaPost, HashTag, InstaImage


def index(request):
    return render(request, 'insta/index.html', {})


def get_all_posts(request):
    #all( ) select * from table
    posts = InstaPost.objects.all()
    return render(request, 'insta/posts.html', locals())


def get_details(request, id):
    post = InstaPost.objects.get(pk=id)
    return render(request, 'insta/post_details.html', locals())
