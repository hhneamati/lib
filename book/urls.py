from django.urls import path , re_path


from . import views


urlpatterns = [
    path ('' , views.BookListView.as_view() ,name = 'index'),
    path('detail/<int:pk>' , views.BookDetailView.as_view() , name = 'bookDetail'),
    
]
