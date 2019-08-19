import operator
from django.shortcuts import render
from .models import Post, Comment, User, Like
from .forms import *

# Create your views here.
def main(request):
    posts = Post.objects.all()
    sort = request.GET.get('sort','')
    if sort == 'new' :       # 최신순
        posts = Post.objects.all()
    elif sort == 'like':        # 좋아요
        ordered_posts = {}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key=operator.itemgetter(1), reverse=True)
        posts = []
        for post in post_list:
            posts.append(post[0])
            
    # elif sort == 'like':
    #     posts = Post.objects.all()
    #     posts = sorted(posts, key=lambda p: p.like_count, reverse=True)

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
    return render(request, 'insta/post_create.html', {'form':form})


#  elif sort == 'likes':        # 좋아요
#             order = {}
#             posts = Post.objects.all()
#             for post in posts :
#                 order[post] = post.post_likes.count()
#             data = sorted(order.items(), key=operator.itemgetter(1), reverse=True)
#             data_list = []
#             for i in data:
#                 data_list.append(i[0])
#             context['object_list'] = data_list[current_page*2-2: current_page*2]