from django.contrib import admin

from .models import RBook, Element


class RBookAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "short_name",
        "description",
        "ver",
        "date_begin",
    )
    list_editable = ("name",)
    search_fields = ("name",)
    list_filter = ("date_begin",)
    empty_value_display = "-пусто-"


class ElementAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "parent_id",
        "code",
        "val",
    )
    list_editable = ("code",)
    search_fields = ("val",)
    list_filter = ("code",)
    empty_value_display = "-пусто-"


admin.site.register(RBook, RBookAdmin)
admin.site.register(Element, ElementAdmin)
