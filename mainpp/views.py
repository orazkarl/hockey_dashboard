from django.shortcuts import render, redirect, HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class HomeView(generic.TemplateView):
    template_name = 'home.html'

@login_required(login_url='/login/')
def start_exam(request):
    user = request.user
    user.is_access = False
    user.save()
    return redirect('http://exam.icehockey.kz/testoriginal.html')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ResultExamView(generic.TemplateView):
    template_name = 'result_exam.html'
