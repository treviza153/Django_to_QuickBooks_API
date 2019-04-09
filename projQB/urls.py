"""projQB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path

from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoView
from appConnection.views.connection import QuickBooksService
from appEnvio.views.views import envio

urlpatterns = [
    path('envio/', envio),
    path('conexao/', DjangoView.as_view(
        services=[QuickBooksService], tns='projetoQB.appConnection.QuickBooksService',
        in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())),
]


