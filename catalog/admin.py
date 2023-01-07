from django.contrib import admin
from catalog.models import Book, Genre,Author,BookInstance, Language
# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Language)
