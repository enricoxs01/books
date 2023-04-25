from django.shortcuts import render,redirect
from .models import Book
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ChapterForm




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
  chapter_form = ChapterForm()
  return render(request, 'books/detail.html', { 'book': book, 'chapter': chapter_form })


def add_chapter(request, book_id):
  form = ChapterForm(request.POST)
  # validate the form
  if form.is_valid():
   #add foreign key to chapter
    new_chapter = form.save(commit=False)
    new_chapter.book_id = book_id
    new_chapter.save()
  return redirect('detail', book_id=book_id)

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
