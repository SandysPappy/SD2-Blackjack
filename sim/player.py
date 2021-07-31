from hand import Hand
import basic_strategy

class BetExceedsStackSize(ValueError):
    pass

class Player():
    def __init__(self, _id, stack_size):
        self._id = _id
        self.stack_size = stack_size # in dollars
        self.hand = Hand()

    def __str__(self):
        return f"id:{self._id}, stack_size:{self.stack_size}, hand:{self.hand}"

    def __repr__(self):
        return f"<Player id={self._id}, stack_size={self.stack_size}, hand:{self.hand}>"

    def add_dollars(self, ammount):
        self.stack_size += ammount

    def subtract_dollars(self, ammount):
        self.stack_size -= ammount

    def get_hand(self):
        return self.hand

    # is only called when a hand has been dealt
    def do_turn(self, up_card_face):
        bs = basic_strategy.get_basic_strategy()

        curr_hand = self.hand.get_hand_value()
        hand_type = curr_hand[0]
        hand_value = curr_hand[1]

        action = bs[hand_type][(hand_value, up_card_face)]

        print(f"With a {curr_hand} and a dealer upcard of {up_card_face}, player {self._id} should {action}")
