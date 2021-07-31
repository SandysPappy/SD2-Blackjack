from card import Card

class Hand:
    def __init__(self, cards_list=None):
        if cards_list is None:
            self.hand = []
        else:
            self.hand = cards_list

    def __str__(self):
        return str([card for card in self.hand])

    def __repr__(self):
        return f"<Hand {self.hand}>"

    def add_card(self, card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand.clear()

    def is_pair(self):
        if len(self.hand) != 2:
            return False
        if self.hand[0].card_face != self.hand[1].card_face:
            return False
        return True

    def is_blackjack(self):
        if len(self.hand) != 2:
            return False
        if self.hand[0].is_ace():
            if self.hand[1].get_hard_value() == 10:
                return True
        if self.hand[1].is_ace():
            if self.hand[0].get_hard_value() == 10:
                return True
        return False

# otherwise returns a tuple giving the hand type
# and the hand value as a string
    def get_hand_value(self):
        if self.is_pair():
            if self.hand[0].is_ace():
                return ('pair', 'A')
            return ('pair', str(self.hand[0].get_hard_value()))

        total_value = 0
        num_aces = 0
        for card in self.hand:
            if card.is_ace():
                num_aces +=1
                continue
            total_value += card.get_hard_value()
        if num_aces == 0:
            return ('hard', str(total_value))
        # now we have to determine if its a hard ace or not
        # Hard hands with aces occur when no Ace can be 11
        # If it's 21, you stand no matter what, so being hard or soft doesn't matter
        if total_value + num_aces-1 + 11 > 21:
            return ('hard', str(total_value + num_aces))
        return ('soft', str(total_value + num_aces-1 + 11))
