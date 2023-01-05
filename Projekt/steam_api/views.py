from django.shortcuts import render, redirect
from .models import User
from .forms import RegisterForm, LoginForm
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


def register(request):
    form = RegisterForm()
    success = None
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username']).exists():
            error = "This username is already taken"
            return render(request, 'steam_api/register.html', {'form': form, 'error': error})
        if User.objects.filter(email=request.POST['email']).exists():
            error = "This email is already taken"
            return render(request, 'steam_api/register.html', {'form': form, 'error': error})
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully !"
    return render(request, 'steam_api/register.html', {'form': form, 'success': success})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username, password=password).exists():
            user = User.objects.get(username=username)
            request.session['user_id'] = user.id
            return redirect('steam_api:home')
    return render(request, 'steam_api/login.html', {'form': form})


def get_user(request):
    return User.objects.get(id=request.session['user_id'])


def home(request):
    if 'user_id' in request.session:
        user = get_user(request)
        return render(request, 'steam_api/home.html', {'user': user})
    else:
        return redirect('steam_api:login')


class UserViewList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Add_Uid(APIView):
    def put(self, request, pk):
        user = get_user(pk)
        user.steam_uid = request
        return Response({"ok"})
