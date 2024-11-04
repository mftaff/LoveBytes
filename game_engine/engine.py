from game_engine import actions
from game_engine import helpers

# Wrapper for helper.compare_hands
def compare_hands(players):
    return helpers.compare_hands(players)

# Resolves the action of a card
#   ply1 is the active player (it's their turn)
#   Returns a victor code (0 means continue play)
def action_resolver(card, state, ply1, ply2, players):
    if ply2.handmaided and card in [1,2,3,5,7]: # Handle special case where handmaid should block card from resolving
        if card == 5:
            return actions.prince(state, players, discard_id=ply1.id)

        print("Your opponent is protected!")
        return 0

    # Handle each card's action
    match card:
        case 0:
            return actions.spy(ply1)
        case 1:
            return actions.guard(ply1, ply2.get_hand())
        case 2:
            return actions.priest(ply2.card_map, ply2.get_hand())
        case 3:
            return actions.baron(players)
        case 4:
            return actions.handmaid(ply1)
        case 5:
            return actions.prince(state, players)
        case 6:
            return actions.chancellor(state, ply1)
        case 7:
            return actions.king(ply1, ply2)
        case 8:
            return 0 # Playing the countess has no effect, so return a no victor code and continue play
        case 9:
            return actions.princess(ply1)
        case _:
            return 0

# Prompt a player to play a card, move it to the discard pile, and resolve the card's action
#   Returns a victor code (0 means continue play)
def turn(state, ply1, ply2, players):
    card = ply1.play_card(helpers.choose_card(ply1))
    state.discard_card(card)

    print('\n\n')
    return action_resolver(card, state, ply1, ply2, players)

# Handle the victory condition. For now compile and return a victory message
def get_victory(victor_id, state, players):
    unique_spy = helpers.calc_spy_victor_condition(players)

    if victor_id == -1:
        v_msg = ["\nIt's a draw!"]
    else:
        v_msg = [f"\nPlayer{victor_id} Wins!"]

    if unique_spy == 0:
        v_msg.append("\nNo unique spy played")
    else:
        v_msg.append(f"\nPlayer{unique_spy} played the only spy! They get an extra point!")

    v_msg.append(f'\n\nFinal Game State:\nPly1: {players[1].pretty_hand}, Ply2: {players[2].pretty_hand}\nDeck: {state.deck}\nDiscards: {state.discards}\nBurn Card: {state.burn_cards}')

    return ''.join(v_msg)