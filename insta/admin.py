from django.contrib import admin
from .models import Post, Comment, User, Like

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','image','caption','created','updated')
    list_filter = ['caption'] # 필터 옵션 제공
    search_fields = ['caption'] # 검색 기능 제공
    fields = ['user','image','caption' ] 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','user','content')
    fields = ['post','user','content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user','post')
    fields = ['user', 'post']