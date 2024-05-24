
from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.libraryHome, name='home' ),
    path('about/', views.libraryAboutUs, name='about'),
    path('books/', views.libraryBooks, name='books'),
    path('book/create', views.libraryCreateBook, name='create'),
    path('book/edite/<int:id>', views.libraryEditBook, name='edit'),
    path('book/delete/<int:id>', views.libraryDeleteBook, name='delete'),
    
]
