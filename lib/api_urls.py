from rest_framework import routers

from book.api_views import BookViewset ,PublisherViewset ,AuthorViewset


router = routers.DefaultRouter()
router.register('Book' , BookViewset , basename='book')
router.register('publisher' , PublisherViewset , basename='publisher')
router.register('author' , AuthorViewset , basename='author')


