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

    try: # liked_post print해보면 현재 사용자가 좋아요 누른 querySet[post.id]이 나옵니다. -> 템플렛단에서 posts for문 돌면서 liked_post와 대조 후 하트/빈하트 출력하려고
        # API의 자세한 설명은 https://docs.djangoproject.com/en/2.2/ref/models/querysets/#values-list 를 참고해주세요
        liked_post =  Like.objects.filter(user=request.user).values_list('post__id', flat=True)
    except:
        liked_post = None

    # +) {post.id : 좋아요갯수} 인 dict 만들어서 좋아요순으로 내림차순(reverse=True)정렬함니다. 왜 dict를 썼냐면 post.id랑 post.좋아요 짝지을려고 | dict의 키값은 유일해야 하니까 post.id로 했음
    # 좋아요의 개수를 통해 정렬하는 로직이며, sorted 함수의 key 인자가 정렬의 기준이 됩니다. -> 요기선 key를 1번째, 즉 dict의 value값으로 줍니다. 0으로 바꾸면 dict의 key가 되겠쥬
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
    # 지금 로그인한 유저가 해당 포스트 좋아요 눌렀으면 -> 지워 | 안눌렀으면 -> 눌러(좋아요 객체 맹글어)