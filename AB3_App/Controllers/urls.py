from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ..controllers import Team_view, Player_view, Relation_view

router = DefaultRouter()
router.register(r'teams', Team_view.Team_view_set)
router.register(r'players', Player_view.Player_view_set)
router.register(r'relations', Relation_view.Relation_view_set)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
