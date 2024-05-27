from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework import APIView



class BookAPIView(APIView):
     def get(self, request):
         return Response({'title': 'Наедине с собой'})



# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer