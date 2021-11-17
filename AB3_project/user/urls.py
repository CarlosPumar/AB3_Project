from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import User_view

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('user/', User_view.as_view()),
]
