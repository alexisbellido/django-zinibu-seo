from django import template
from django.conf import settings

from znbmain.models import BaseContent
from znbmain.utils import get_absolute_url, is_production


register = template.Library()

@register.inclusion_tag('znbseo/robots_snippet.html')
def robots_snippet(request, object=None, index=True):
    """
    Set robots meta to index, follow for production only for home page and
    live articles.
    """
    meta_robots = "noindex, nofollow"
    if is_production and index:
        if (object and object.status == BaseContent.LIVE_STATUS) or (request.path == '/'):
            meta_robots = "index, follow"
    return {
        'meta_robots': meta_robots
    }

@register.inclusion_tag('znbseo/canonical.html')
def canonical(request, object=None):
    if not object:
        url = request.path
    return {
        'url': get_absolute_url(object, False)
    }

@register.inclusion_tag('znbseo/google_analytics.html')
def google_analytics():
    return {
        'is_production': is_production,
        'tracking_id': getattr(settings, 'ZNBSEO_GA_ID', '')
    }
