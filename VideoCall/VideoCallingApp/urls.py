from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name= "login"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('meeting/', views.videocall_view, name="meeting"),
    path('logout/', views.logout_view, name="logout"),
]





