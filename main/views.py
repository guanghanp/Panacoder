from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category, Tag
from django.views.generic import  DetailView, ListView
import markdown
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from comment.models import Comment

class IndexView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'main/main.html'
    paginate_by = 2

    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-total_views','-id')
        return ('-created')

class CategoryView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'main/main.html'
    paginate_by = 2

    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-total_views','-id')
        return ('-created')
    
    def get_queryset(self, **kwargs):
        queryset = super(CategoryView, self).get_queryset()
        cate = get_object_or_404(Category, id=self.kwargs.get('pk'))
        return queryset.filter(category=cate)
        
    def get_context_data(self, **kwargs):
        context_data = super(CategoryView, self).get_context_data()
        cate = get_object_or_404(Category, id=self.kwargs.get('pk'))
        context_data['filterType'] = "Category"
        context_data['filterInstance'] = cate
        return context_data

class TagView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'main/main.html'
    paginate_by = 2

    def get_ordering(self):
        sort = self.kwargs.get('sort')
        if sort == 'v':
            return ('-total_views','-id')
        return ('-created')
    
    def get_queryset(self, **kwargs):
        queryset = super(TagView, self).get_queryset()
        tag = get_object_or_404(Tag, id=self.kwargs.get('pk'))
        return queryset.filter(tags=tag)
        
    def get_context_data(self, **kwargs):
        context_data = super(TagView, self).get_context_data()
        tag = get_object_or_404(Tag, id=self.kwargs.get('pk'))
        context_data['filterType'] = "Tag"
        context_data['filterInstance'] = tag
        return context_data

class ArticleView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'main/detail.html'

    def get_context_data(self, **kwargs):
        context_data = super(ArticleView, self).get_context_data()
        article = context_data['article']

        # increment total views for this article
        article.total_views += 1
        article.save(update_fields=['total_views'])

        md = markdown.Markdown(
            extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ]
        )
        article.body = md.convert(article.body)
        comments = Comment.objects.filter(article=article.id)
        context_data['toc'] = md.toc
        context_data['comments'] = comments
        return context_data
