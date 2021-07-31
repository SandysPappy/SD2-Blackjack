from hand import Hand
import basic_strategy

class BetExceedsStackSize(ValueError):
    pass

class InvalidSeat(IndexError):
    pass

class Player():
    def __init__(self, _id, stack_size):
        self._id = _id
        self.stack_size = stack_size # in dollars
        self.hand = Hand()
        self.curr_bet = None

    def __str__(self):
        return f"id:{self._id}, stack_size:{self.stack_size}, hand:{self.hand}"

    def __repr__(self):
        return f"<Player id={self._id}, stack_size={self.stack_size}, hand:{self.hand}>"

    def receive_card(self, card):
        self.hand.add_card(card)

    def clear_hand(self):
        self.hand.clear_hand()

    def add_dollars(self, ammount):
        self.stack_size += ammount

    def subtract_dollars(self, ammount):
        self.stack_size -= ammount

    def get_hand(self):
        return self.hand

    def clear_bet(self):
        self.curr_bet = None

    def set_bet(self, ammount):
        self.curr_bet = ammount

    # overwrites player index, be careful
    def take_seat(self, index, table):
        if index < 0 or index > 6:
            raise InvalidSeat(f" please insert a seat position between 0 and 6, you gave: {index}")
        table.player_list[index] = self
