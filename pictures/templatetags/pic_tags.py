from django import template
import datetime
from django.utils import timezone
from django.db.models import Count
from ..models import Picture , Category

register = template.Library()

@register.simple_tag()
def best_month():
    last_month = Picture.objects.filter(created__lte=timezone.now(), created__gt=timezone.now()-datetime.timedelta(days=30))

    best_month = last_month.annotate(total_likes=Count('likes')).order_by('-total_likes')[:1]
    best_month = best_month[0]
    return best_month


@register.simple_tag()
def get_random_cat():
    rand_cat = Category.objects.order_by('?')
    return rand_cat[:4]

@register.inclusion_tag('include/manageNav.html')
def manage_nav(request):
    return {'user':request.user}