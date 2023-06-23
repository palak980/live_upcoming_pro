from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('register/',views.UserRegistrationView.as_view()),
    path('login/',views.LoginAPI.as_view()),


]