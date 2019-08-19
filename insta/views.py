from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def main(request):
    posts = Post.objects.order_by('-created')
    sort = request.GET.get('sort','')
    if sort == 'new' :       # 최신순
        posts = Post.objects.order_by('-created')
    elif sort == 'like':
        posts = Post.objects.order_by('created')
    return render(request, 'insta/main.html', {'posts': posts})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'insta/new.html', {'form':form})
