import operator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, User, Like
from .forms import PostForm, CommentForm

def main(request):
    posts = Post.objects.all()
    sort = request.GET.get('sort','')
    comment_form = CommentForm()

    if sort == 'new' : # 글 작성 시각의 내림차순으로 정렬
        posts = Post.objects.all()
    elif sort == 'like': # 좋아요 개수의 내림차순으로 정렬
        ordered_posts = {}
        post_list = Post.objects.all()
        for post in post_list:
            ordered_posts[post] = post.like_count
        post_list = sorted(ordered_posts.items(), key=operator.itemgetter(1), reverse=True)
        posts = []
        for post in post_list:
            posts.append(post[0])

    try:
        # API의 자세한 설명은 https://docs.djangoproject.com/en/2.2/ref/models/querysets/#values-list 를 참고해주세요
        liked_post =  Like.objects.filter(user=request.user).values_list('post__id', flat=True)
    except:
        liked_post = None

    # 좋아요의 개수를 통해 정렬하는 로직이며, sorted 함수의 key 인자가 정렬의 기준이 됩니다.
    # 따라서 post의 like_count 필드를 기준으로 정렬을 수행합니다.
    # elif sort == 'like':
    #     posts = Post.objects.all()
    #     posts = sorted(posts, key=lambda p: p.like_count, reverse=True)

    return render(request, 'insta/main.html', {
        'posts': posts , 
        'comment_form': comment_form, 
        'liked_post':liked_post
    })

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    return render(request, 'insta/post_create.html', {
        'form': form
    })


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

def like(request,post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
        except:
            Like.objects.create(user=request.user, post=post)
            
    return redirect('main')