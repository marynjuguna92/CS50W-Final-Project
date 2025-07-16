from django.urls import path
from . import views, contact
from .views import robots_txt

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', contact.submit, name='contact_submit'),
    path('robots.txt', robots_txt, name='robots_txt'),
]
