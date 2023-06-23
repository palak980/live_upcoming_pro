from django.urls import path
from .views  import *
from social_media import views

urlpatterns=[

    path('get_post_social/', views.Social_View, name='get_post_social'),
    path('get_put_patch_delete_socialByID/<int:pk>', views.Social_View2, name='get_put_patch_delete_socialByID'),

    path('get_post_action/', views.Action_View, name='get_post_action'),
    path('get_put_patch_delete_actionByID/<int:pk>', views.Action_View2, name='get_put_patch_delete_actionByID'),

]