from django.urls import path
from .views  import *
from contact import views

urlpatterns=[

    path('get_post_social/', views.Mymsgview, name='get_post_social'),
    path('get_put_patch_delete_socialByID/<int:pk>', views.Mymsgview2, name='get_put_patch_delete_socialByID'),


]