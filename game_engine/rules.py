def print_rules():
    print(
"""*************************
Game Rules

Initial setup:
Shuffle the deck. Deal one card to each player. Deal a card to the burn pile.
Choose a player to go first. Play proceeds clockwise.

Turn order:
Draw a card, discard a card from your hand, resolve that card's action.

Win conditions:
    1) Have the highest value card once the deck is empty and each player has one card left.
    2) Be the last player standing (ie all other players are eliminated by a guard, etc).

Cards:
0_Spy        x2: If you are the only player to play/discard a spy from your hand, you get an extra point at the end of the round.
1_Guard      x6: Guess the card of an opponent. If you guess correct they are eliminated. You cannot guess they have a guard.
2_Priest     x2: Look at an opponent's card
3_Baron      x2: Compare hands with an oppponent. The lower handed player is eliminated. A draw doesn't eliminate anyone.
4_Handmaid   x2: You may not be targeted by any action until the start of your next turn.
5_Prince     x2: Choose an opponent. They discard their card and redraw. If the deck is empty, draw the burn_card.
6_Chancellor x2: Draw two cards. Then put two cards back at the end of the deck. You choose the order of those two cards.
7_King       x1: Swap hands with an opponent.
8_Countess   x1: At the start of your turn, you must play this card if you have a king or prince in your hand.
9_Princess   x1: If you play or discard this card you are eliminated.

In-game help:
On your turn, type "help n" (where n is a card's integer value) for info on that card
*************************"""
)

# Given index returns that card's information
def card_help(card_id):
    return [
        "0_Spy x2: If you are the only player to play/discard a spy from your hand, you get an extra point at the end of the round.",
        "1_Guard x6: Guess the card of an opponent. If you guess correct they are eliminated. You cannot guess they have a guard.",
        "2_Priest x2: Look at an opponent's card",
        "3_Baron x2: Compare hands with an oppponent. The lower handed player is eliminated. A draw doesn't eliminate anyone.",
        "4_Handmaid x2: You may not be targeted by any action until the start of your next turn.",
        "5_Prince x2: Choose an opponent. They discard their card and redraw. If the deck is empty, draw the burn_card.",
        "6_Chancellor x2: Draw two cards. Then put two cards back at the end of the deck. You choose the order of those two cards.",
        "7_King x1: Swap hands with an opponent.",
        "8_Countess x1: At the start of your turn, you must play this card if you have a king or prince in your hand.",
        "9_Princess x1: If you play or discard this card you are eliminated.",
    ][card_id]
