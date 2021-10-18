from ..utils.data import POSIBLE_STATES

# Get all the posible player state names: 'avaiable', 'doubtful', etc


def get_posible_states():

    values = list(POSIBLE_STATES.values())

    posible_states = []

    for value in values:
        posible_states.extend(value['names'])

    return posible_states


# Return True if the tweet is a informative tweet abaout the state of a player
# Return False otherwise

def is_status_player(text):

    enc = False
    i = 0
    text_lower = text.lower()
    states = get_posible_states()

    if "(" in text_lower:
        while enc == False and i < len(states):
            if states[i] in text_lower:
                enc = True
            i += 1

    return enc

# Return the player name in a tweet


def get_player_name(text):

    player_name = text.split("(")[0][:-1]

    return player_name

# Return the player state in a tweet


def get_state(text):

    values = list(POSIBLE_STATES.values())

    for value in values:

        if any(state in text for state in value['names']):
            return value['code']

    return False
