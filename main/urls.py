from django.urls import path
from .views import IndexView,ArticleView,CategoryView,TagView,ArchiveView, AboutView

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('view/', IndexView.as_view(), {'sort': 'v'}, name='article_list_view'),
    path('detail/<int:pk>/', ArticleView.as_view(), name='detail'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('category/<slug:slug>/view', CategoryView.as_view(), {'sort': 'v'}, name='category_view'),
    path('tag/<slug:slug>/', TagView.as_view(), name='tag'),
    path('tag/<slug:slug>/view', TagView.as_view(), {'sort': 'v'}, name='tag_view'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('about/', AboutView, name='about')
    # path('create/', views.article_create, name='article_create'),
    # path('delete/<int:id>/', views.article_delete, name='article_delete'),
]