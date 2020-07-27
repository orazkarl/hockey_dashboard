from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm




def logout_user(request):
    logout(request)
    return redirect('account_login')




