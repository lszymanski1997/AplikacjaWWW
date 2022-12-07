import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Druzyna(models.Model):
    class Kraj(models.TextChoices):
        POLSKA = "PL", _("Polska")
        NIEMCY = "DE", _("Niemcy")
        USA = "US", _("Stany Zjednoczone")

    nazwa = models.CharField(max_length=50)
    kraj = models.CharField(max_length=2, choices=Kraj.choices, default=Kraj.POLSKA)

    class Meta:
        ordering = ["nazwa"]
        verbose_name_plural = "Drużyny"

    def __str__(self):
        return str(self.nazwa) + " (" + str(self.kraj) + ")"


class Osoba(models.Model):
    class MIESIAC(models.TextChoices):
        STYCZEN = "1", _("Styczeń")
        LUTY = "2", _("Luty")
        MARZEC = "3", _("Marzec")
        KWIECIEN = "4", _("Kwiecień")
        MAJ = "5", _("Maj")
        CZERWIEC = "6", _("Czerwiec")
        LIPIEC = "7", _("Lipiec")
        SIERPIEN = "8", _("Sierpień")
        WRZESIEN = "9", _("Wrzesień")
        PAZDZIERNIK = "10", _("Październik")
        LISTOPAD = "11", _("Listopad")
        GRUDZIEN = "12", _("Grudzień")

    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=100)
    miesiac_urodzenia = models.CharField(max_length=2, choices=MIESIAC.choices, default=MIESIAC.STYCZEN)
    data_dodania = models.DateField(auto_now_add=True)
    druzyna = models.ForeignKey(Druzyna, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.imie) + " " + str(self.nazwisko)

    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Osoby"
