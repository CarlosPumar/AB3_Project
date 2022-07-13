from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Team_view_set

router = DefaultRouter()
router.register(r'teams', Team_view_set)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
