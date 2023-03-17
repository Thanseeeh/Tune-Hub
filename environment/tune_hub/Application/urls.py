from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path("signup/", views.signup, name="signup"),
    path('index/', views.index, name='index'),
    path('admins/', views.admins),
]
