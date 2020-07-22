from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Data Model for Article Post
class ArticleColumn(models.Model):

    # title for column
    title = models.CharField(max_length=100, blank=True)
    # time of creation
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# Data Model for Article Post
class ArticlePost(models.Model):

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    body = models.TextField()
    total_views = models.PositiveIntegerField(default=0)
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='article'
    )
    image = ProcessedImageField(
        upload_to='article/%Y%m%d',
        processors=[ResizeToFit(width=400)],
        format='JPEG',
        null=True,
        blank=True,
        options={'quality': 100},
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])

