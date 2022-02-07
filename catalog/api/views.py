from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from reference_book.models import Element, RBook
from .serializers import ElementSerializer, RBookSerializer


class RBookViewSet(viewsets.ModelViewSet):
    queryset = RBook.objects.all()
    serializer_class = RBookSerializer


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementRBookViewSet(viewsets.ModelViewSet):
    serializer_class = ElementSerializer

    def get_queryset(self):
        reference_book_id = self.kwargs.get("reference_book_id")
        parent_id = get_object_or_404(RBook, id=reference_book_id)
        new_queryset = Element.objects.filter(parent_id=parent_id)
        return new_queryset
