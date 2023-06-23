
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.db.models import Q
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import random
# from .utils import *
from rest_framework import generics, status
from django.contrib.auth import authenticate

# Create your views here.
class UserRegistrationView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationsSerializer
    permission_class = ['IsAuthenticated']


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        #print(data)
        email = data.get('email')
        #print(email)
        password = data.get('password')
        user=authenticate(email=email,password=password)
        print(user)
        if user is not None and user.is_admin:
            return Response({'Message':'Admin Login Successfully!!', 'status':status.HTTP_200_OK})
        elif user is not None and user.is_staff:
            return Response({'Message':'Staff Login Successfully!!', 'status':status.HTTP_200_OK})
        elif user is not None and user.is_user:
            return Response({'Message':'User Login Successfully!!', 'status':status.HTTP_200_OK})

        else:
            return Response({'errors':'Email or Password are not valid','status':status.HTTP_400_BAD_REQUEST})
        