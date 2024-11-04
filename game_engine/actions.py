from game_engine import helpers

# These functions resolve the action for each card in the deck

def spy(player):
    print(f'Player{player.id} has played a Spy!')
    player.played_spy = True
    return 0

def guard(ply1, opponents_card):
    while True:
        u = input('Guess opponents card (integer)\n> ')
        try:
            i = int(u)

            if i == 1:
                print("Cannot guess a guard. Try again")
            elif i == opponents_card:
                print("Correct guess!")
                return ply1.id
            else:
                print("Nope, wrong guess")
                return 0
        except:
            print("Input an integer")

def priest(card_map, opponents_card):
    print(f"Your opponent has a {card_map[opponents_card]}")
    return 0

def baron(players):
    return helpers.compare_hands(players)

def handmaid(player):
    print(f"Player{player.id} is protected until the start of their next turn.")
    player.handmaided = True
    return 0

def prince(state, players, discard_id=None):
    if discard_id:
        return resolve_prince(state, players, discard_id)

    player_ids = list(players.keys())

    while True:
        u = input(f'Which player to discard? {player_ids}\n> ')
        try:
            i = int(u)

            if i in player_ids:
                return resolve_prince(state, players, i)
            else:
                print("Choose a player id")
        except:
            print("Input an integer")

def chancellor(state, player):
    while player.hand_size < 3:
        if state.deck_empty():
            break
        player.add_card(state.draw_card())

    if player.hand_size == 1:
        print("Deck is empty, discarding Chancellor")
        return 0

    while player.hand_size > 1:
        print("Choose a card to return to the end of the deck:")
        u = input(f'Hand: {player.pretty_hand}\n(Select {"1, 2, or 3" if player.hand_size == 3 else "1 or 2"})\n> ')
        try:
            i = int(u) - 1

            if i in range(player.hand_size):
                state.append_to_deck(player.play_card(i))
            else:
                print("Choice out of range")
        except:
            print("Input an integer")

    return 0

def king(ply1, ply2):
    temp1, temp2 = ply1.play_card(), ply2.play_card() # remove hands to temp
    ply1.add_card(temp2)
    ply2.add_card(temp1)

    print(f"You and your opponents swap hands.\nYour new hand: {ply1.pretty_hand}")
    return 0

# Handled as a one liner in engine.action_resolver
# def countess():
#     return 0

def princess(player):
    print(f'Player{player.id} discarded a princess. They Lose!')
    return 1 if player.id == 2 else 2 # this logic only works for 2 players

### Helper functions ###

# Handles discarding, redrawing, and checking for win conditions once the prince card chooses a player target
def resolve_prince(state, players, i):
    print(f"Discarding player{i}'s hand and redrawing")

    # Remove players card to discard pile
    old_card = players[i].play_card()
    state.discard_card(old_card)

    if old_card == 9: # player i loses
        return princess(players[i])

    if old_card == 0: # A spy was discarded, so update that player's spy flag
        spy(players[i])

    # Redraw the players hand and continue play
    players[i].add_card(state.draw_card(allow_burn_draw=True))
    return 0