from django import template
import datetime
from django.db.models import Count
from ..models import Picture

register = template.Library()

@register.simple_tag()
def best_month():
    last_month = Picture.objects.filter(craeted__lte=datetime.datetime.today(), craeted__gt=datetime.datetime.today()-datetime.timedelta(days=30))

    best_month = last_month.annotate(total_likes=Count('likes')).order_by('-total_likes')[:1]
    best_month = best_month[0]
    return best_month
