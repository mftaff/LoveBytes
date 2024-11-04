import random

class State:
    card_map = ["0_spy", "1_guard", "2_priest", "3_baron", "4_handmaid", "5_prince", "6_chancellor", "7_king", "8_countess", "9_princess"]

    def __init__(self):
        self.deck = _get_new_deck()
        self.discards = []
        self.burn_cards = [self.draw_card()]

    # Remove and return a card from deck
    def draw_card(self, deck_index=0, allow_burn_draw=False):
        if not self.deck and allow_burn_draw: # Handle edge case where prince triggers a redraw but the deck is empty
            # if not self.burn_cards # If playing with ruleset that allows empty burn_cards
            #     return self.discards.pop(random.randint(0,len(self.discards)-1))
            return self.burn_cards.pop()

        if deck_index >= len(self.deck):
            print("index exceeded deck, drawing from top")
            deck_index = 0

        return self.deck.pop(deck_index)

    def append_to_deck(self, card):
        self.deck.append(card)

    # Append a card into discards (newest card at the end of the list)
    def discard_card(self, card):
        self.discards.append(card)

    def deck_empty(self):
        return True if not self.deck else False

    def get_last_played(self):
        if self.discards:
            return self.card_map[self.discards[-1]]
        else:
            return "N/A"

# returns a new shuffled deck
def _get_new_deck():
    d = [0,0,1,1,1,1,1,1,2,2,3,3,4,4,5,5,6,6,7,8,9]
    random.shuffle(d)
    return d
