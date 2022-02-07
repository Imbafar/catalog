from django.urls import include, path
from rest_framework import routers

from .views import ElementRBookViewSet, ElementViewSet, RBookViewSet

app_name = "api"

router_v1 = routers.DefaultRouter()

router_v1.register("reference_book", RBookViewSet)
router_v1.register("element", ElementViewSet)
router_v1.register(
    r"reference_book/((?P<reference_book_id>[^/.]+))/element",
    ElementRBookViewSet,
    basename="elements",
)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
