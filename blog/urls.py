from django.contrib.sitemaps.views import sitemap
from django.urls import path
from . import views
from blog.sitemap import ArticleSitemap

app_name = 'blog'

urlpatterns = [
    path('', views.post_list,name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list,name='post_list_by_tag'),
    # path('', views.PostListView.as_view(),name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_details, name='post_detail'),
    path('<int:post_id>/share/',views.post_share ,name='post_share'),
    path('<slug:slug>/comment/', views.post_comment, name='post_comment'),
    path('sitemap.xml', sitemap, {'sitemaps': {'article' : ArticleSitemap}},
     name='django.contrib.sitemaps.views.sitemap'),
    path('search/', views.post_search, name='post_search'),

]