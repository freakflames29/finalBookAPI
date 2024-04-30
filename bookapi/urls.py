from django.urls import path
from .views import AuthorView,AuthorDetailView,BookView,AuthorGenView,BookDetailView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path("authors/",AuthorView.as_view()),
    path("authors/<int:pk>/",AuthorDetailView.as_view()),
    path("books/",BookView.as_view()),
    path("books/<int:pk>/",BookDetailView.as_view()),
    path("token/",obtain_auth_token)
]


