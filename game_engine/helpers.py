from game_engine import rules
import re

# Compare two players' cards and return the id of the player with the higher value card.
#   A draw returns -1 
def compare_hands(players):
    if players[1].get_hand() > players[2].get_hand():
        return 1
    elif players[1].get_hand() == players[2].get_hand():
        return -1
    else:
        return 2

# Print player's hand and prompts them for the index of the card they want to play.
def choose_card(player):
    # Checks for countess condition where she must be played
    forced_countess = 8 in player.hand and (5 in player.hand or 7 in player.hand)

    print(f'Hand: {player.pretty_hand}')
    print(f'{"You must play your 8_countess!" if forced_countess else "Which card do you want to play?"}')

    while True:
        u = input('Choose card (1 or 2)\n> ')

        # Check if user inputs "help <n>" and return that card info than restart the loop
        m = re.match(r"^help ([0-9])$", u)
        if m:
            print(f"{rules.card_help( int(m.group(1)) )}\n")
            continue

        # Try and parse user's input as a card index
        try:
            i = int(u) - 1

            if i in [0,1]:
                if forced_countess and i != player.hand.index(8): # Handle countess special case
                    print("You must choose the 8_countess!")
                else:
                    return i # Return the index of the card to choose
            else:
                print("Enter 1 or 2")
        except:
            print("Input an integer")

# return player id if only that player discarded a spy. Else return 0
def calc_spy_victor_condition(players):
    if players[1].played_spy and not players[2].played_spy:
        return 1
    elif players[2].played_spy and not players[1].played_spy:
        return 2
    return 0
