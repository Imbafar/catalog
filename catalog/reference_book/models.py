from django.db import models

class RBook(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="наименование",
    )
    short_name = models.CharField(
        max_length=10,
        verbose_name="короткое наименование",
    )
    description = models.TextField(
        verbose_name="описание",
    )
    ver = models.CharField(
        max_length=200,
        verbose_name="версия",
    )
    date_begin = models.DateField(
        verbose_name="дата начала действия справочника",
    )

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"
        unique_together = ('name', 'ver',)

    def __str__(self):
        return self.name


class Element(models.Model):
    parent_id = models.ForeignKey(
        RBook,
        on_delete=models.SET_NULL,
        null=True,
        related_name='elements',
        verbose_name="родительский идентификатор",
    )
    code = models.CharField(
        blank=False,
        max_length=200,
        verbose_name="код элемента",
    )
    val = models.CharField(
        blank=False,
        max_length=200,
        verbose_name="значение элемента",
    )

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"

    def __str__(self):
        return self.code
