from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from article.models import ArticlePost


# Data Model for Article Post
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]
