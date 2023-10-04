from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class PostModel(models.Model):
    """帖子model"""
    title = models.CharField(max_length=255)
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    """评论model"""
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'

    def __str__(self):
        return self.content
