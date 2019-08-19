import operator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, User, Like
from .forms import PostForm, CommentForm

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
    comment_form = CommentForm()

    # elif sort == 'like':
    #     posts = Post.objects.all()
    #     posts = sorted(posts, key=lambda p: p.like_count, reverse=True)

    return render(request, 'insta/main.html', {'posts': posts , 'comment_form': comment_form})

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


def create_comment(request,post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            
            return redirect('main')