"""awareness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from article.views import home, awareness, about, donate,\
    article, concepts, yomedi, zen, qigong, mnemonics, books, media, search
from accounts.views import login_view, register_view
urlpatterns = [
    path('admin/', admin.site.urls),

    path('awareness', awareness, name='awareness'),
    path('concepts', concepts, name='concepts'),
    path('yomedi', yomedi, name='yomedi'),
    path('zen', zen, name='zen'),
    path('qigong', qigong, name='qigong'),
    path('mnemonics', mnemonics, name='mnemonics'),
    path('books', books, name='books'),
    path('media', media, name='media'),

    path('search', search, name='search'),



    re_path('article/(?P<pid>[0-9]+)', article, name='article'),
    path('login', login_view, name='login'),
    path('about', about, name='about'),
    path('donate', donate, name='donate'),
    path('register', register_view, name='register'),
    path('', home),

]
