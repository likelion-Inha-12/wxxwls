from django.db import models 
from django.contrib.auth.models import User

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50) 
    content = models.TextField(null=True, blank=True) 
    create_at = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(Member, verbose_name="멤버", primary_key=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length = 200)
    post = models.ForeignKey(Post, verbose_name="포스트", on_delete=models.CASCADE)
    member = models.ForeignKey(Member, verbose_name="멤버", on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.content


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)




