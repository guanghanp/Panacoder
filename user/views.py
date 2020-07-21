from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm

# login view
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            # authenticate user
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("Username or password does not match our record.")
        else:
            return HttpResponse("Username or password is not valid.")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'user/login.html', context)
    else:
        return HttpResponse("Please use GET or POST for this URL.")

# logout view
def user_logout(request):
    logout(request)
    return redirect("article:article_list")

def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # set password
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # log in as new user 
            login(request, new_user)
            return redirect("article:article_list")
        else:
            return HttpResponse("invalid entry is entered")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'user/register.html', context)
    else:
        return HttpResponse("Please use GET or POST for this URL.")