from rest_framework import serializers
from .models import Gamer, Game, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gamer
        fields = ('name', 'email', 'username', 'steam_uid')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('game_name', 'gid')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('pk', 'title', 'text', 'gid', 'username')
