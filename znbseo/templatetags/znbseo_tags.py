from django import template
from django.conf import settings
from django.contrib.sites.models import Site

from znbmain.models import Article


register = template.Library()

@register.inclusion_tag('znbseo/robots_snippet.html')
def robots_snippet(request, object=None, index=True):
    """
    Set robots meta to index, follow for production only for home page and
    live articles.
    """
    meta_robots = "noindex, nofollow"
    running_env = getattr(settings, 'ZNBSEO_IS_PRODUCTION', False)
    if running_env and index:
        if (object and object.status == Article.LIVE_STATUS) or (request.path == '/'):
            meta_robots = "index, follow"
    return {'meta_robots': meta_robots}

@register.inclusion_tag('znbseo/canonical.html')
def canonical(request, object=None):
    if object:
        url = object.get_absolute_url()
    else:
        url = request.path
    url = 'http://%s%s' % (Site.objects.get_current().domain, url)
    return {'url': url}
