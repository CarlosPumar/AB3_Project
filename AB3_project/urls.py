"""ab3_project URL Configuration

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
import sys
from django.contrib import admin
from ab3_project.twitter.stream import Stream_Twitter
from ab3_project.utils.data import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, ID_ACCOUNT
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

""" Importar urls de las diferentes entidades """

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('ab3_project.team.urls'), name='teams'),
    path('api/', include('ab3_project.player.urls'), name='players'),
    path('api/', include('ab3_project.relation.urls'), name='relations'),
    path('api/', include('ab3_project.banker.urls'), name='banker'),
    path('api/', include('ab3_project.user.urls'), name='users'),

    path('api/', include('ab3_project.utils.urls'), name='utils'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
