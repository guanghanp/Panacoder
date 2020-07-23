from django.shortcuts import render, redirect
from .models import Article
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
        context_data['article']=article
        context_data['toc'] = md.toc
        context_data['comments'] = comments
        print(article.body, md.toc)
        return context_data

# def article_create(request):
#     # 判断用户是否提交数据
#     if request.method == "POST":
#         # 将提交的数据赋值到表单实例中
#         article_post_form = ArticlePostForm(data=request.POST)
#         # 判断提交的数据是否满足模型的要求
#         if article_post_form.is_valid():
#             # 保存数据，但暂时不提交到数据库中
#             new_article = article_post_form.save(commit=False)
#             # 指定数据库中 id=1 的用户为作者
#             # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
#             # 此时请重新创建用户，并传入此用户的id
#             new_article.author = User.objects.get(id=1)
#             # 将新文章保存到数据库中
#             new_article.save()
#             # 完成后返回到文章列表
#             return redirect("article:article_list")
#         # 如果数据不合法，返回错误信息
#         else:
#             return HttpResponse("Opps, Something went wrong. Please check your syntax.")
#     # 如果用户请求获取数据
#     else:
#         # 创建表单类实例
#         article_post_form = ArticlePostForm()
#         # 赋值上下文
#         context = { 'article_post_form': article_post_form }
#         # 返回模板
#         return render(request, 'article/create.html', context)

# @login_required(login_url='/user/login/')
# def article_delete(request, id):
#     article = Article.objects.get(id=id)
#     if request.user != article.author:
#         return HttpResponse("Sorry, you have no rights to delete this article.")
#     article.delete()
#     return redirect("article:article_list")
