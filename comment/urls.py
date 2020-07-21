from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('new/<int:article_id>/', views.new_comment, name='new_comment'),
]