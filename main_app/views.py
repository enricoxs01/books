from django.shortcuts import render,redirect
from .models import Book,Bookmark
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ChapterForm, BookmarkForm




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
  #bookmarks = book.bookmark.all()
  id_list = book.bookmark.all().values_list('id')
  unassociated_bookmarks = Bookmark.objects.exclude(id__in=id_list)
  
  return render(request, 'books/detail.html', { 
    'book': book, 
    'chapter': chapter_form,
    'bookmarks': unassociated_bookmarks })

def assoc_bookmark(request, book_id, bookmark_id):

  Book.objects.get(id=book_id).bookmark.add(bookmark_id)
  return redirect('detail',book_id=book_id)

def unassoc_bookmark(request, book_id, bookmark_id):

  Book.objects.get(id=book_id).bookmark.remove(bookmark_id)
  return redirect('detail',book_id=book_id)


def add_chapter(request, book_id):
  form = ChapterForm(request.POST)
  # validate the form
  if form.is_valid():
   #add foreign key to chapter
    new_chapter = form.save(commit=False)
    new_chapter.book_id = book_id
    new_chapter.save()
  return redirect('detail', book_id=book_id)

#def bookmark_index(request):
# bookmarks = Bookmark.objects.all()
#  return render(request, 'bookmarks/index.html', {
#    'bookmarks': bookmarks
#  })


class BookCreate(CreateView):
  model = Book
  fields = ['title','author','description','date']
  success_url = '/books'

class BookUpdate(UpdateView):
  model = Book
  fields = ['author', 'description', 'date']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books'

  
class BookmarkCreate(CreateView):
  model = Bookmark
  fields = '__all__'
  success_url = '/'

class BookmarkList(ListView):
  model = Bookmark

class BookmarkDetail(DetailView):
  model=Bookmark

class BookmarkDelete(DeleteView):
  model = Bookmark
  success_url = '/'

class BookmarkUpdate(UpdateView):
  model = Bookmark
  fields = ['color', 'material']
