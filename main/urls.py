from django.urls import path
from .views import IndexView,ArticleView

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='article_list'),
    path('view/', IndexView.as_view(), {'sort': 'v'}, name='article_list_view'),
    path('detail/<int:pk>/', ArticleView.as_view(), name='detail'),
    # path('create/', views.article_create, name='article_create'),
    # path('delete/<int:id>/', views.article_delete, name='article_delete'),
]