from django.urls import path

from . import views

app_name = "reference_book"

urlpatterns = [
    path(
        "",
        views.index,
        name="index",
    ),
    path(
        "reference_book/<int:reference_book_id>/",
        views.reference_book_detail,
        name="reference_book_detail",
    ),
    path(
        "create_reference/",
        views.reference_book_create,
        name="reference_book_create",
    ),
    path(
        "element/<int:element_id>/",
        views.element_detail,
        name="element_detail",
    ),
    path(
        "reference_book/<int:reference_book_id>/edit/",
        views.reference_book_edit,
        name="reference_book_edit",
    ),
    path(
        "element/<int:element_id>/edit/",
        views.element_edit,
        name="element_edit",
    ),
    path(
        "create_element/",
        views.element_create,
        name="element_create",
    ),
]
