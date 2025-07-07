from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # 회원가입 후 자동 로그인
        return redirect('/')

    return render(request, 'accounts/signup.html')

from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            next_url = request.POST.get('next','/')
            return redirect(next_url if next_url else '/')
        else:
            return render(request, 'accounts/login.html', {'error': '아이디 또는 비밀번호가 틀렸습니다.'})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

