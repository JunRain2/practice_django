from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') # form의 입력값을 개별적으로 가지고 싶을때 사용.
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password =raw_password) # 사용자 인증을 담당
            login(request, user) # autenticate로 생성하자마자 login/ 로그인을 담당
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})