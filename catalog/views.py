from django.shortcuts import render
from catalog.models import Author,Book, BookInstance, Genre
from django.views import generic

# Create your views here.

def index(request):

    num_books = Book.objects.all().count()
    num_instances= BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status="a").count()
    num_author = Author.objects.count()
    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available': num_instances_available,
        'num_authors':num_author,
    }

    return render(request, 'catalog/index.html', context=context )

class BookListView(generic.ListView):
    model = Book
    # queryset =  Book.objects.filter(title__icontains='tuk')

    # template_name = "catalog/book_list.html"
