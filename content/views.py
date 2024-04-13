from django.shortcuts import render
from .models import Movie, Theater, Showtime, Reserve, Purchase
from .serializers import MovieSerializer, TheaterSerializer, ShowtimeSerializer,ReserveSerializer, PurchaseSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    
    
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MovieListCreate(generics.ListCreateAPIView):
    queryset  = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
   


class MovieRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination



class TheaterListCreate(generics.ListCreateAPIView):
    queryset  = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = [IsAuthenticated]

class TheaterRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = [IsAuthenticated]


class ShowtimeListCreate(generics.ListCreateAPIView):
    queryset  = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAuthenticated]

class ShowtimeRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Showtime.objects.all()
    serializer_class = ShowtimeSerializer
    permission_classes = [IsAuthenticated]

class ReserveListCreate(generics.ListCreateAPIView):
    queryset  = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]
   

class ReserveRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]
    


class PurchaseListCreate(generics.ListCreateAPIView):
    queryset  = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    
class PurchaseRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
