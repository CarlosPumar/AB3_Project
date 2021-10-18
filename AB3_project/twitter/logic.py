from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from . import parse
from ..player.models import Player
from ..relation.models import Relation
from ..relation.serializer import Relation_serializer
from ..banker.models import Banker
from ..banker.serializer import Banker_serializer
import json


def manage_message(text):

    # Comprobación si es un tweet de cambio de estado
    if parse.is_status_player(text):

        player_name = parse.get_player_name(text)
        state = parse.get_state(text)

        # Comprobación si existe el jugador en la base de datos con nombre 'player_name'
        if Player.manager_extend.player_exists(player_name):

            player_state = Player.manager_extend.get_state_from_player(
                player_name)

            Player.manager_extend.modify_state(player_name, state)

            # Si esta dentro de la siguiente casuistica
            if (player_state == "AV" and ((state == "QU") or (state == "RO") or (state == "DB"))) or (player_state == "QU" and state == "RO"):

                information = get_information(player_name)

                # Envío de información
                send_data_from_twitter(information)


# Enviar informacion al grupo de twitter
def send_data_from_twitter(data):

    try:
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "twitter",
            {
                "type": "player.message",
                "text": data
            },
        )
    except RuntimeError:
        print("No se ha podido conectar")

#  Return information that will be send to the extension


def get_information(player_name):

    relations = Relation.manager_extend.get_relation_from_player(
        player_name)

    relations_serializer = Relation_serializer(
        relations, many=True)

    banker = Banker.objects.get(pk=1)

    banker_serializer = Banker_serializer(banker)

    information = {
        'banker': banker_serializer.data,
        'relations': relations_serializer.data,
    }

    return json.dumps(information)
