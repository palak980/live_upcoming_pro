from django.urls import path
from .views  import *
from trending_tweets import views

urlpatterns=[

    path('Tweets_news/', views.Tweets_news, name='Tweets_news'),

]