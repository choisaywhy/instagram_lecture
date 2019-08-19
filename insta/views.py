from django.shortcuts import render,get_object_or_404
from .models import Post, Comment, Like
# Create your views here.

def index(request):
    post = Post.objects.all().order_by('updated_at')[:5]
    context = {
        'posts':post,
    }
    return render(request, 'post/post_list.html', context)

def detail(request, post_id):
    post = get_objects_or_404(Post, pk =post_id)
    context = {
        'posts' : post
    }
    return render(request,'post/detail.html', context )

def create(request):    
    pass
