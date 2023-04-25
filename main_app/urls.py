# Add the include function to the import
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about, name='about'),
    path('books/',views.book_index, name='index'),
#    path('books/', BookList.as_view(), name='books_index',
    path('books/<int:book_id>/', views.book_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
    path('cats/<int:book_id>/add_chapter/', views.add_chapter, name='add_chapter'),

]
