from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "name", "price", "buyinglink", "rating", "author_name", "author"]

    def get_author_name(self, obj):
        return obj.author.name


class AuthorSerializer(serializers.ModelSerializer):
    book_names = serializers.SerializerMethodField()
    # books = BookSerializer()
    class Meta:
        model = Author
        fields = ["id", "name", "gender", "book_names"]

    def get_book_names(self, obj):
        books = obj.book_set.all()
        book_names = [book.name for book in books]
        return book_names
