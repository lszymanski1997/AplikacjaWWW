import json

import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Gamer, Game, Review
from .forms import RegisterForm, LoginForm
from .serializers import UserSerializer, GameSerializer, ReviewSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from .api_key import api_key
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@csrf_exempt
def register(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    if User.objects.filter(username=username).exists():
        return JsonResponse("user already exists", safe=False)
    else:
        gamer = User.objects.create_user(username=username, password=password)
        gamer.save()
        return JsonResponse("created succesfully", safe=False)


@csrf_exempt
def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    username = body['username']
    password = body['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        return JsonResponse('ok', safe=False)
    else:
        return JsonResponse('404', safe=False)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def game_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return JsonResponse({"games": serializer.data})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def game_detail(request, pk):
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GameSerializer(game)
        return JsonResponse({"game": serializer.data})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return JsonResponse({'reviews': serializer.data})


@api_view(['GET', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def review_detail(request, pk):
    try:
        review = Review.objects.get(pk=pk)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return JsonResponse({"rewiew": serializer.data})
    if request.method == 'DELETE':
        user = request.user
        if user == review.username:
            review.delete()
            return JsonResponse("deleted", safe=False)
        else:
            return JsonResponse("failed", safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request):
    if request.method == 'POST':
        username = request.user
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body['title']
        text = body['text']
        gid = Game.objects.get(gid=int(body['gid']))
        review = Review(title=title, text=text, gid=gid, username=username)
        review.save()
        return JsonResponse("review succesfull", safe=False)


def refresh_game_list(request):
    gameget = requests.get(
        'https://api.steampowered.com/ISteamApps/GetAppList/v0002/?key=' + api_key + '&format=json').json()[
        'applist']
    gamelist = gameget['apps']
    for game in gamelist:
        if game['name'] != '':
            namestr = str(game['name'])
            gidint = int(game['appid'])
            if Game.objects.filter(game_name=game['name']).exists():
                pass
            else:
                g = Game(game_name=namestr, gid=gidint)
                g.save()
    return JsonResponse("refreshed", safe=False)
