from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
# Create your views here.



def libraryHome(request):
    return render(request, 'library/home.html')

def libraryAboutUs(request):
    return render(request, 'library/aboutus.html')

def libraryBooks(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'library/books.html', context)

def libraryCreateBook(request):
    form = BookForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('library:books')
    
    return render(request, 'library/crear.html', context)

def libraryEditBook(request, id):
    book = Book.objects.get(pk=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    context = {
        'form': form
    }
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('library:books')

    return render(request, 'library/editar.html', context)


def libraryDeleteBook(request, id):
    book = Book.objects.filter(pk=id)
    if book:
        book.delete()
        
    return redirect('library:books')

