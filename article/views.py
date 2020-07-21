from django.shortcuts import render, redirect
from .models import ArticlePost
import markdown
# 引入HttpResponse
from django.http import HttpResponse
# 引入刚才定义的ArticlePostForm表单类
from .forms import ArticlePostForm
# 引入User模型
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def article_list(request):
    article_list = ArticlePost.objects.all()

    paginator = Paginator(article_list,2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles':articles}
    return render(request,'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    article.body = markdown.markdown(article.body,
    extensions=[
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)


def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("Opps, Something went wrong. Please check your syntax.")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'article/create.html', context)

def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")
