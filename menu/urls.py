from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.page_view, {"page_slug": "index"}, name='index'),
    path('company/', views.page_view, {"page_slug": "company"}, name='company'),
    path('company/about/', views.page_view, {"page_slug": "company_about"}, name='company_about'),
    path('company/team/', views.page_view, {"page_slug": "company_team"}, name='company_team'),
    path('company/jobs/', views.page_view, {"page_slug": "company_jobs"}, name='company_jobs'),
    path('services/', views.page_view, {"page_slug": "services"}, name='services'),
    path('services/web-dev', views.page_view, {"page_slug": "web_dev"}, name='web_dev'),
    path('services/web-dev/frontend', views.page_view, {"page_slug": "frontend"}, name='frontend'),
    path('services/web-dev/backend', views.page_view, {"page_slug": "backend"}, name='backend'),
    path('services/mobile/', views.page_view, {"page_slug": "mobile"}, name='mobile'),
    path('services/mobile/android', views.page_view, {"page_slug": "android"}, name='android'),
    path('services/mobile/ios', views.page_view, {"page_slug": "ios"}, name='ios'),
    path('blog/', views.page_view, {"page_slug": "blog"}, name='blog'),
    path('blog/it_news/', views.page_view, {"page_slug": "it_news"}, name='it_news'),
    path('blog/forum/', views.page_view, {"page_slug": "forum"}, name='forum'),


]
