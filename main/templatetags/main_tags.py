from django import template

register = template.Library()

from django.utils import timezone
import math

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

@register.inclusion_tag('main/tags/list.html',takes_context=True)
def load_article_list(context):
    return context