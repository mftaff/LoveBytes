class Player:
    card_map = ["0_spy", "1_guard", "2_priest", "3_baron", "4_handmaid", "5_prince", "6_chancellor", "7_king", "8_countess", "9_princess"]

    def __init__(self, id, is_human, initial_card):
        self.human = is_human # expect bool
        self.id = id
        self.played_spy = False
        self.handmaided = False
        self.hand = [initial_card]
        self.pretty_hand = [self.card_map[initial_card]]
        self.hand_size = 1

    # Add a card to player's hand
    #   Updates hand, pretty_hand, hand_size
    def add_card(self, card):
        self.hand.append(card)
        self.pretty_hand.append(self.card_map[card])
        self.hand_size += 1

    # Remove and return a card from player's hand
    #   Updates hand, pretty_hand, hand_size
    def play_card(self, index=0):
        if index >= len(self.hand):
            print("index exceeded hand, drawing from top")
            index = 0

        self.pretty_hand.pop(index)
        card = self.hand.pop(index)
        self.hand_size -= 1
        return card

    def get_hand(self):
        return self.hand[0]
