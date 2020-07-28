from django.contrib import admin
from .models import Article,Category,Tag
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    date_hierarchy = 'created'
    exclude = ('views',)
    list_display = ('id', 'title', 'author', 'created', 'updated')
    list_display_links = ('title',)
    list_filter = ('created', 'category')
    list_per_page = 50 
    filter_horizontal = ('tags',) 

    # the users can only see their own articles
    def get_queryset(self, request):
        qs = super(ArticleAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('name',)