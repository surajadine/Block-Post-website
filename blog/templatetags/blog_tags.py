from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()
from ..models import Post
import markdown as md

@register.simple_tag
def totalPost():
    return Post.objects.count()

@register.inclusion_tag('blog/post/latest_post.html')
def show_latest_posts(count):
    latest_post = Post.objects.order_by('-publish')[:count]
    return {'latest_post':latest_post}


@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value,extensions=['markdown.extensions.fenced_code'])