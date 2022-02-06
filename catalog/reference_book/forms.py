from django import forms

from .models import RBook, Element


class RBookForm(forms.ModelForm):
    class Meta:
        model = RBook
        fields = (
            "name",
            "short_name",
            "description",
            "ver",
            "date_begin",
        )
        labels = {
            "name": "наименование",
            "short_name": "короткое наименование",
            "description": "описание",
            "ver": "версия",
            "date_begin": "дата начала действия справочника",
        }
        help_texts = {
            "name": "Введите наименование",
            "short_name": "Введите короткое наименование",
            "ver": "Укажите версию",
            "date_begin": "Введите дату начала действия справочника",
            "description": "Введите описание",
        }
        verbose_name = "Форма справочника"


class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = (
            "parent_id",
            "code",
            "val"
        )
        labels = {
            "parent_id": "родительский идентификатор",
            "code": "код элемента",
            "val": "значение элемента",
        }
        help_texts = {
            "parent_id": "Введите сообщение",
            "code": "Введите код элемента",
            "val": "Введите значение элемента",
        }
        verbose_name = "Форма элемента'"
        
