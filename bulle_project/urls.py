"""
URL configuration for bulle_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include

from .views import IndexPage
from .views import InfoPage
from .views import ContactoPage
from .views import ShopPage
from .views import MayoristaPage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", IndexPage.as_view(),name="index"),
    path("info/", InfoPage.as_view(),name="info"),
    path("shop/", ShopPage.as_view(),name="shop"),
    path("contacto/", ContactoPage.as_view(),name="contacto"),
    path("mayorista/", MayoristaPage.as_view(),name="mayorista"),
    path("tienda/", include("tienda_app.urls"))
]

