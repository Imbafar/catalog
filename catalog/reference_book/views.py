from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect

from .models import RBook, Element
from .forms import RBookForm, ElementForm


def index(request):
    reference_book = RBook.objects.all()
    paginator = Paginator(reference_book, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "reference_book/index.html", context)

def reference_book_detail(request, reference_book_id):
    reference_book = get_object_or_404(RBook, id=reference_book_id)
    elements = reference_book.elements.all()
    paginator = Paginator(elements, settings.POSTS_FOR_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    form = RBookForm()
    context = {
        'reference_book': reference_book,
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'reference_book/reference_book_detail.html', context)

def reference_book_create(request):
    form = RBookForm(request.POST or None)
    if form.is_valid():
        # reference_book = form.save(commit=False)
        # reference_book.save()
        form.save()
        return redirect('reference_book:index')
    return render(request, 'reference_book/create_reference_book.html', {'form': form})

def element_detail(request, element_id):
    element = get_object_or_404(Element, id=element_id)
    form = ElementForm()
    context = {
        'element': element,
        'form': form,
    }
    return render(request, 'reference_book/element_detail.html', context)

def reference_book_edit(request, reference_book_id):
    reference_book = get_object_or_404(RBook, id=reference_book_id)

    form = RBookForm(
        request.POST or None,
        instance=reference_book
    )
    if form.is_valid():
        form.save()
        return redirect('reference_book:reference_book_detail', reference_book_id)
    context = {'form': form, 'reference_book': reference_book, 'is_edit': True}
    return render(request, 'reference_book/create_reference_book.html', context)

def element_create(request):
    form = ElementForm(request.POST or None)
    if form.is_valid():
        # element = form.save()
        # element.save()
        form.save()
        return redirect('reference_book:index')
    return render(request, 'reference_book/create_element.html', {'form': form})

def element_edit(request, element_id):
    element = get_object_or_404(Element, id=element_id)
    print(element)

    form = ElementForm(
        request.POST or None,
        instance=element
    )
    if form.is_valid():
        print('HEREE')
        form.save()
        return redirect('reference_book:element_detail', element_id)
    print('OMG')
    context = {'form': form, 'element': element, 'is_edit': True}
    return render(request, 'reference_book/create_element.html', context)
