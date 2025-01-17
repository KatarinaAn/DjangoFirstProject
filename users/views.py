from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
  if request.method == 'GET':
    form = LoginForm()
    return render(request, 'login.html', {'form': form})

  elif request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user:
        login(request, user)
        messages.success(request, 'You are logged in')
        return redirect('home')
    messages.error(request, 'invalid username/password')
    return render(request, 'login.html', {'form': form})


# Create your views here.
def sign_out(request):
  logout(request)
  messages.success(request, 'You are logged out')
  return redirect('login')