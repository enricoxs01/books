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
    path('books/<int:book_id>/add_chapter/', views.add_chapter, name='add_chapter'),
    path('books/<int:book_id>/assoc_bookmark/<int:bookmark_id>/', views.assoc_bookmark, name='assoc_bookmark'),
    path('books/<int:book_id>/unassoc_bookmark/<int:bookmark_id>/', views.unassoc_bookmark, name='unassoc_bookmark'),

   
   # path('bookmark/', views.bookmark_index, name = 'bookmark_index'),
    path('bookmark/', views.BookmarkList.as_view(), name='bookmark_index'),
    path('bookmark/<int:pk>/', views.BookmarkDetail.as_view(), name='bookmark_detail'),
    path('bookmark/create', views.BookmarkCreate.as_view(), name = 'bookmark_create'),
    path('bookmark/<int:pk>/delete', views.BookmarkDelete.as_view(), name = 'bookmark_delete'),
    path('bookmark/<int:pk>/update/', views.BookmarkUpdate.as_view(), name='bookmark_update')
]
