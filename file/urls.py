from django.urls import path
from . import views
urlpatterns = [
    path('Profileview/',views.Profileview),
    path('GetProfileview/',views.GetProfileview),
    path('putProfileview/<int:pk>',views.putProfileview),
]
