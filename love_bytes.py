from classes import state as st, player as pl
from game_engine import engine as game
from game_engine import rules
# from game_engine import helpers

state = st.State()

players = {
    1: pl.Player(1, True, state.draw_card()),
    2: pl.Player(2, True, state.draw_card()),
}

rules.print_rules()

turn_count = -1
victor = 0
while victor == 0:
    turn_count += 1
    player_id = (turn_count % (len(players)) + 1 )
    player = players[player_id]
    opponent = players[2 if player_id == 1 else 1]
    print(f'\n*************************\nTurn: {turn_count}.\nLast Discard: {state.get_last_played()}\nPlayer{player_id} to play')

    ### run game here ###

    # Reset player's handmaid flag at the start of their turn
    if player.handmaided:
        player.handmaided = False

    player.add_card(state.draw_card())

    if player.human:
        victor = game.turn(state, player, opponent, players)
    else:
        # Implement a computer player
        pass
    
    # Compare hands to check winner if no victor and the deck is empty
    if not victor and state.deck_empty():
        victor = game.compare_hands(players)

victory = game.get_victory(victor, state, players)
print(victory)