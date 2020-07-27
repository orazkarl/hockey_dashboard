from django.urls import path, include
from . import views

urlpatterns = [

    # path('login/', views.LoginView.as_view(), name='login'),
    # path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
