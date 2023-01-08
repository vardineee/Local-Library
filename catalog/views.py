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
    paginate_by = 2
    # queryset =  Book.objects.filter(title__icontains='tuk')

    # template_name = "catalog/book_list.html"


class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
