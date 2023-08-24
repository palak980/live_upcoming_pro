"""live_upcoming_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('cricinfo/',include("live_upcoming_app.urls")),
    # path('sports_news/',include("sports_news.urls")),
    path('social_media/',include("social_media.urls")),
    path('trending_tweets/',include("trending_tweets.urls")),
    path('profile/',include('file.urls')),
    # path('space/', include('space.urls')),
    path('manual_news/', include('manual_news.urls')),
    path('role/', include('role.urls')),
    path('subscription/', include('subscription.urls')),
    path('contact/', include('contact.urls'))


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
