from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from rest_framework import generics, mixins
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AuthorGenView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorView(APIView):
    def get(self, rq):
        authors = Author.objects.all()
        auth_ser = AuthorSerializer(authors, many=True)
        return Response(auth_ser.data, status=200)

    def post(self, rq):
        author_ser = AuthorSerializer(data=rq.data)
        if author_ser.is_valid():
            author_ser.save()
            return Response(author_ser.data, status=201)
        return Response(author_ser.errors, status=400)


"""views for id based operation"""


class AuthorDetailView(APIView):
    def detail(self, pk):
        try:
            author = Author.objects.get(pk=pk)
            if author:
                return author
        except:

            raise Http404

    def get(self, rq, pk):
        author = self.detail(pk)
        author_ser = AuthorSerializer(author)
        return Response(author_ser.data, status=200)

    def post(self, rq, pk):
        author = self.detail(pk)
        authoser = AuthorSerializer(author, data=rq.data, partial=True)
        if authoser.is_valid():
            authoser.save()
            return Response(authoser.data, status=200)
        return Response(authoser.errors, status=400)

    def delete(self, rq, pk):
        author = self.detail(pk)
        author.delete()
        return Response([], status=204)


"""book views"""


class BookView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, rq):
        return self.list(rq)

    def post(self, rq):
        return self.create(rq)


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SignupView(APIView):
    pass
