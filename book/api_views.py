from rest_framework import  viewsets

from .serializers import BookSerializer , PublisherSerializer , AuthorSerializer

from .models import Book ,Publisher , Author

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class PublisherViewset(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer