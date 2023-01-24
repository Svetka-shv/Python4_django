"""py4dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>Домашня сторінка</h1>")

def progress(request: HttpRequest, start: int, count: int, step: int) -> HttpResponse:
    end = start + step * (count - 1)
    l = []
    for i in range(start, end + step, step):
        l.append(i)
    return HttpResponse(f"<h1>Послідовність: {l}</h1>")

def fibonachi(request: HttpRequest, n: int) -> HttpResponse:
    fib1 = fib2 = 1
    n = n - 2
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return HttpResponse(f"Значення елемента: {fib2}")

def gretting(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"<h1>Greetign, {name}</h1>")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('progression/<int:start>/<int:count>/<int:step>/', progress),
    path('fib/<int:n>', fibonachi),
    path('greeting/<name>/', gretting)
]
