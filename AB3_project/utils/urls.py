from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import States_view

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('states/', States_view.as_view()),
]
