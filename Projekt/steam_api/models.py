from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    steam_uid = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
