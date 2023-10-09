from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserForm
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print("login is valid")
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        login_form = LoginForm()
    context = {'login_form': login_form}
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('login')
    else:
        form = UserForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')