from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def Mysubsview(request):
    if request.method == 'GET':
        snippets = Mysubs.objects.all()
        serializer = MysubsSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MysubsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE','PATCH'])
def Mysubsview2(request, pk):
    try:
        snippet = Mysubs.objects.get(pk=pk)
    except Mysubs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MysubsSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MysubsSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        serializer = MysubsSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
