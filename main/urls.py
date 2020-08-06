from django.urls import path
from .views import IndexView,ArticleView,CategoryView,TagView,ArchiveView, AboutView

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('view/', IndexView.as_view(), {'sort': 'v'}, name='article_list_view'),
    path('detail/<int:pk>/', ArticleView.as_view(), name='detail'),
    path('category/<int:pk>/', CategoryView.as_view(), name='category'),
    path('category/<int:pk>/view', CategoryView.as_view(), {'sort': 'v'}, name='category_view'),
    path('tag/<int:pk>/', TagView.as_view(), name='tag'),
    path('tag/<int:pk>/view', TagView.as_view(), {'sort': 'v'}, name='tag_view'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('about/', AboutView, name='about')
    # path('create/', views.article_create, name='article_create'),
    # path('delete/<int:id>/', views.article_delete, name='article_delete'),
]