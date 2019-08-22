from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser): 
    profile  = models.ImageField()


class Post(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE) 
    image = models.ImageField()
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated'] # updated 필드를 기준으로 내림차순 정렬

    def __str__(self):
        return self.caption

    # like 갯수를 세기 위한 property 구현
    @property
    def like_count(self):
        return self.like_set.count()  

                               
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user  = models.ForeignKey(User, on_delete=models.CASCADE) 
    content = models.TextField()


class Like(models.Model): 
    user  = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)