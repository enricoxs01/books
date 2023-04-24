from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView




# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', {
    'books': books
  })

def book_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  return render(request, 'books/detail.html', { 'book': book })

class BookCreate(CreateView):
  model = Book
  fields = '__all__'
  success_url = '/books'

class BookUpdate(UpdateView):
  model = Book
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['author', 'description', 'date']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books'