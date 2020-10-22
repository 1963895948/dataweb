"""dataweb URL Configuration

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
from django.urls import path,re_path
from django_web import views
from django_web.views import index,bj,sh,gz,cd,wh,cs,download,download1,updata,login,rigister


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/index/', index, name='index'),
    path('rigister/index/', index, name='index'),
    path('index/bj/', bj, name='bj'),
    path('index/sh/', sh, name='sh'),
    path('index/gz/', gz, name='gz'),
    path('index/cd/', cd, name='cd'),
    path('index/wh/', wh, name='wh'),
    path('index/cs/', cs, name='cs'),
    path('updata/', updata, name='updata'),
    path('index/download/', download, name='download'),
    path('index/download1/', download1, name='download1'),
    path('login/', login, name='login'),
    path('rigister/', rigister, name='rigister'),
]
