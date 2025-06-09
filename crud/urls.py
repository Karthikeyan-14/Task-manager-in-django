"""
URL configuration for new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [

# path is used to redirect to the function in the views by the function name
#path('sitename',views.(function name),name='url name')
    
    path('',views.start),
    path('reg',views.go_reg, name='register'),
    path('log',views.go_log, name='login'),
    path('dash',views.go_dash,name='dashboard'),

    path('regsave',views.register),
    path('logsave',views.login),
    path('save_task',views.task_save,name='save_task'),

    path('delete',views.delete,name='delete_task'),
    path('update',views.update,name='update_task')

]
