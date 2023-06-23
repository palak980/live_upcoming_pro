from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework import generics
# Create your views here.
@api_view(['POST'])
def Profileview(request):
    serializer=profileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def GetProfileview(request):
    request.method == 'GET'
    model = profilemodel.objects.all()
    serializer = profileSerializer(model, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def putProfileview(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        model= profilemodel.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = profileSerializer(model)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = profileSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    if request.method=='PUT':
        model=profilemodel.objects.get(pk=pk)
        serializer=profileSerializer(model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
        
    if request.method=='DELETE':
        model=profilemodel.objects.get(pk=pk)
        model.delete()





