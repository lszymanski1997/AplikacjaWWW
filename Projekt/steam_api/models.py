from django.db import models
from django.contrib.auth.models import User


class Gamer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Game(models.Model):
    game_name = models.CharField(max_length=255)
    gid = models.IntegerField()

    class Meta:
        ordering = ['game_name']

    def __str__(self):
        return self.game_name


class Review(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=5000)
    gid = models.ForeignKey(Game, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
