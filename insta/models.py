from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser): 
    profile  = models.ImageField()

class Post(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE) 
    image = models.ImageField()
    caption = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.caption

    @property # like 갯수를 세기 위해서 
    def like_count(self):
        return self.like_set.count()  # 모델의 릴레이션 셋 -> 기본값 모델명_set
                               
class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user  = models.ForeignKey(User,on_delete=models.CASCADE) 
    content = models.TextField()


class Like(models.Model): 
    user  = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=models.CASCADE)