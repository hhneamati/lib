from django.views import generic 

from .models import (
    Author ,
    Book ,
    Genre ,
     )
     


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        context["my_book_list"] = Book.objects.all() 
        return context
    
class BookDetailView(generic.DetailView):
    model = Book
   