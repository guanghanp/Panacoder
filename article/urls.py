from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('list/', views.IndexView.as_view(), name='article_list'),
    path('view/', views.IndexView.as_view(), {'sort': 'v'}, name='article_list_view'),
    path('detail/<int:pk>/', views.ArticleView.as_view(), name='article_detail'),
    path('create/', views.article_create, name='article_create'),
    path('delete/<int:id>/', views.article_delete, name='article_delete'),
]