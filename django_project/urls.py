"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from appdoeduardo import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset_form.html',
             email_template_name='password_reset_email.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('users/login/', views.login_user, name="login"),
    path('users/logout/', views.logout_user, name="logout"),
    path('users', views.create_user),
    path('listusers', views.list_users),
    path('users/update/<user_id>', views.update_user),
    path('users/delete/<user_id>', views.delete_user),
    path('machines', views.create_machine),
    path('machines/update/<id>', views.update_machine),
    path('machines/delete/<id>', views.delete_machine),
    path('features', views.create_feature),
    path('features/update/<id>', views.update_feature),
    path('features/delete/<id>', views.delete_feature),
    path('distros', views.create_distro),
    path('distros/update/<id>', views.update_distro),
    path('distros/delete/<id>', views.delete_distro),
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
