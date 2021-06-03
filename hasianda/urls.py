"""farm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from .import views

app_name = 'hasianda'

urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("register/", views.register, name = "register"),
    path("login/", views.login, name = "login"),
    path("logout/",views.logout,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("addfarm/",views.addfarm,name="addfarm"),
    path("options/",views.options,name="options"),
    path("logout/",views.logout,name="logout"),
    path("listfarm/",views.listfarm,name="listfarm"),
    path("choosefarm/",views.choosefarm,name="choosefarm"),
    
]
