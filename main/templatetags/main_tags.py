
from django import template
from django.utils import timezone
from ..models import Article, Category, Tag
from django.db.models.aggregates import Count
import math

register = template.Library()

@register.filter(name='timesince_en')
def time_since_en(value):
    now = timezone.now()
    diff = now - value

    if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
        return 'just now'

    if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
        if diff.seconds // 60 == 1:
            return "1 minute ago"
        return str(math.floor(diff.seconds / 60)) + " minutes ago"

    if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
        if diff.seconds // 3600 == 1:
            return "1 hour ago"
        return str(math.floor(diff.seconds / 3600)) + " hours ago"

    if diff.days >= 1 and diff.days < 30:
        if diff.days == 1:
            return "1 day ago"
        return str(diff.days) + " days ago"

    if diff.days >= 30 and diff.days < 365:
        if diff.days // 30 == 1:
            return "1 month ago"
        return str(math.floor(diff.days / 30)) + " months ago"

    if diff.days >= 365:
        if diff.days // 365 == 1:
            return "1 year ago"
        return str(math.floor(diff.days / 365)) + " years ago"

@register.filter(name='toMonth')
def toMonth(value):
    Months = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
    return Months[value]

@register.inclusion_tag('main/tags/list.html',takes_context=True)
def load_article_list(context):
    return context

@register.simple_tag
def get_category():
    return Category.objects.annotate(total=Count('article')).filter(total__gt=0)

@register.simple_tag
def get_tag_list():
    return Tag.objects.annotate(total=Count('article')).filter(total__gt=0)



