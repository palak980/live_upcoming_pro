from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def Social_View(request):
    if request.method == 'GET':
        snippets = SocialClass.objects.all()
        serializer = SocialSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Social_View2(request, pk):
    try:
        snippet = SocialClass.objects.get(pk=pk)
    except SocialClass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = SocialSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#ACTION_VIEW

@api_view(['GET', 'POST'])
def Action_View(request):
    if request.method == 'GET':
        snippets = ActionClass.objects.all()
        serializer = ActionSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Action_View2(request, pk):
    try:
        snippet = ActionClass.objects.get(pk=pk)
    except SocialClass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActionSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = ActionSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)