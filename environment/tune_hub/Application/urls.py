from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("signup/", views.signup, name="signup"),
    path('index/', views.index, name='index'),
    path('adminpanel/', views.admin, name='admin'),
    path('admin/', views.login_admin, name='login_admin'),
]
