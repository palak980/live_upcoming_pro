from django.urls import path
from .views  import *
from subscription import views

urlpatterns=[

    path('get_post_social/', views.Mysubsview, name='get_post_social'),
    path('get_put_patch_delete_socialByID/<int:pk>', views.Mysubsview2, name='get_put_patch_delete_socialByID'),


]