from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
import requests


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

        ip = get_client_ip(request)
        print(ip)
        user = request.user
        user.ip_address = str(ip)
        user.save()


        return super().get(request, *args, **kwargs)


@login_required(login_url='/login/')
def start_exam(request):
    user = request.user
    user.is_access = False
    user.save()
    return redirect('http://examtest.icehockey.kz/')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ResultExamView(generic.TemplateView):
    template_name = 'result_exam.html'
