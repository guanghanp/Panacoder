from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField 
from django.db.models.signals import pre_delete
import cloudinary
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

# Data Model for Category
class Category(models.Model):

    # name for catagory
    name = models.CharField(max_length=30,unique=True)
    # time of creation
    created = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug':self.slug})

# Article tag
class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    # return all the articles in this tag
    def get_article_list(self):
        return Article.objects.filter(tags=self)

    def get_absolute_url(self):
        return reverse('main:tag', kwargs={'slug':self.slug})


# Data Model for Article Post
class Article(models.Model):

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    body = models.TextField()
    total_views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='article'
    )
    # image = ProcessedImageField(
    #     upload_to='article/%Y%m%d',
    #     processors=[ResizeToFit(width=400)],
    #     format='JPEG',
    #     null=True,
    #     blank=True,
    #     options={'quality': 100},
    # )
    image = CloudinaryField(
        'image',
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(Tag,blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])

# Data Model for About
class About(models.Model):
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'About'

