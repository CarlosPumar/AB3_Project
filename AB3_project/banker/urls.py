from django.urls import path
from .views import Banker_view


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('banker/', Banker_view.as_view(), name='banker-detail'),
]
