from django.contrib import admin
from .models import Osoba, Druzyna


class OsobaAdmin(admin.ModelAdmin):
    list_display = ["imie", "nazwisko", "miesiac_urodzenia", "druzyna"]
    list_filter = ["druzyna", "data_dodania"]


class DruzynaAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "kraj"]
    list_filter = ["kraj"]


# Register your models here.
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Druzyna, DruzynaAdmin)
