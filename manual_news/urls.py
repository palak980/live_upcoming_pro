from django.urls import path
from .views  import *
from manual_news import views

urlpatterns=[

    path('get_post_social/', views.Manual_View, name='get_post_social'),
    path('get_put_patch_delete_socialByID/<int:pk>', views.Manual_View2, name='get_put_patch_delete_socialByID'),

    path('get_post_twitter/', views.Twitter_View, name='get_post_social'),
    path('get_put_patch_delete_twitterByID/<int:pk>', views.Twitter_View2, name='get_put_patch_delete_socialByID'),

]