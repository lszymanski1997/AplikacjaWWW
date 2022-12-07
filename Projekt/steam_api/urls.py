from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    steam_id = models.CharField(max_length=2, choices=MIESIAC.choices, default=MIESIAC.STYCZEN)
    data_dodania = models.DateField(auto_now_add=True)
