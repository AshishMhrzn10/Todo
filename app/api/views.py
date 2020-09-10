from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TodoSerializer, UserSerializer
from ..models import Todo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


@api_view(['GET'])
@permission_classes([AllowAny])
def apiOverview(request):
    api_urls = {
        'List': '/posts/',
        'Detail View': '/posts/<str:pk>/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def PostView(request):
    posts = Todo.objects.all().order_by('-id')
    serializer = TodoSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def DetailView(request, pk):
    posts = Todo.objects.get(id=pk)
    serializer = TodoSerializer(posts)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateView(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateView(request, pk):
    posts = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=posts, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteView(request, pk):
    posts = Todo.objects.get(id=pk)
    posts.delete()

    return Response("Item successfully deleted.")