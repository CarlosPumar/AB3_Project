from django.views import View
from django.http import JsonResponse
from ..models.Team import Team
from ..query import Team_query


class Team_list_view(View):

    def get(self, request):
        team_list = Team_query.get_team_list()
        return JsonResponse(team_list, safe=False)


class Team_view(View):

    def get(self, request, id):
        team = Team_query.get_team_by_id(id)
        return JsonResponse(team)
