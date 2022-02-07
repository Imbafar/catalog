from reference_book.models import Element, RBook
from rest_framework import serializers


class RBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = RBook
        exclude = ("id",)


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        exclude = ("id",)
