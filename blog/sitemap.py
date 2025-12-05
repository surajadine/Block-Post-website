from django.contrib.sitemaps import Sitemap
from .models import Post

class ArticleSitemap(Sitemap):
    changefreq = "weekly" # Optional: how frequently the page is likely to change
    priority = 0.7        # Optional: the priority of this URL relative to other URLs on your site (0.0 to 1.0)
    def items(self):
        return Post.objects.all()
      
    def lastmod(self, obj):
        return obj.updated