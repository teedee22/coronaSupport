"""coronaSupport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from supportteam.views import (
    index,
    login_user,
    logout_user,
    register_page,
    register_new_user,
    scan_volunteer,
    scan_requests,
    assign_requests,
    handle_sms,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
    path("register", register_page, name="register"),
    path("register_new_user", register_new_user, name="register_user"),
    path("scan_volunteer", scan_volunteer, name="scan_volunteer"),
    path("scan_requests", scan_requests, name="scan_requests"),
    path("assign_requests", assign_requests, name="assign_requests"),
    path("handle_sms", handle_sms, name="handle_sms"),
]
