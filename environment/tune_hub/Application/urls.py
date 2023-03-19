from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("signup/", views.signup, name="signup"),
    path('index/', views.index, name='index'),
    path('adminpanel/', views.admin, name='admin'),
    path('admin/', views.login_admin, name='login_admin'),
    path('adminpanel/delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('adminpanel/update_user/<int:user_id>/', views.update_user, name='update_user'),
]

