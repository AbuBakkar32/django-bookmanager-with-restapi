from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    # API
    path('api/', include(router.urls)),
    # Views
    path('', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book_new'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
