from django.urls import path, include
from django.contrib import admin
from portfolio import views
from portfolio.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from portfolio.views import robots_txt



sitemaps = {   
     'static': StaticViewSitemap(),
}

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
