from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('result_exam', views.ResultExamView.as_view(), name='result_exam'),
    path('start_exam', views.start_exam, name='start_exam'),
]
