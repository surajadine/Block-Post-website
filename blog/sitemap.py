from django.contrib.sitemaps import Sitemap
from .models import Post

class ArticleSitemap(Sitemap):
    def items(self):
        return Post.objects.all()
      
    def lastmod(self, obj):
        return obj.lastedit_date