from django.urls import path
from djbooks import views
from djbooks.views import Link, NewAuthor, EditAuthor, ProfileView
from django.urls import include

urlpatterns = [
    path("", views.home, name="home"),
    path("publisher/<pub_id>", views.publisher, name="publisher"),
    path("book/<book_id>", views.book, name='book'),
    path("books", views.book_list, name='books'),
    path("authors", NewAuthor.as_view(), name='authors'),
    path("new-publisher", views.get_publisher, name='new-publisher'),
    path("new-author", views.get_author, name='new-author'),
    path("links", Link.as_view(), name='links'),
    path ("new-author/<author_id>", EditAuthor.as_view(), name="edauthor"),
    path("new-author/<author_id>/delete", views.delete_author, name="deleteauthor"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='profile')
]
