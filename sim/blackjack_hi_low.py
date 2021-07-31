from shoe import Shoe
from hand import Hand
from card import Card
from player import Player
from dealer import Dealer
import basic_strategy

class InvalidSeat(IndexError):
    pass

# we're forcing players to only bet on one spot
class Table:
    def __init__(self, num_decks, deck_pen, min_bet, max_bet):
        self.num_decks = num_decks
        self.deck_pen = deck_pen
        self.shoe = Shoe(num_decks, deck_pen)

        self.player_list = [None] * 7
        self.dealer = Dealer()

        self.count = {'running_count': 0, 'true_count': 0}
        self.strategy = basic_strategy.get_basic_strategy()
        self.min_bet = min_bet
        self.max_bet = max_bet

    def __str__(self):
        string = "Game state\n"

        string += f"min bet is {self.min_bet}\n"
        string += f"max bet is {self.max_bet}\n"
        string += "\n"

        string += f"Running count: {self.count['running_count']}\n"
        string += f"True count: {self.count['true_count']}\n"
        string += "\n"

        string += f"Dealer's upcard: {self.dealer.get_up_card()}\n"
        string += "\n"

        string += f"Players list: \n"
        for player in self.player_list:
            if player:
                string += f"\tSeat {self.player_list.index(player)}\t{player}\n"
        string += "\n"

        string += f"shoe size: {self.num_decks}\n"
        string += f"deck penetration: {self.deck_pen}\n"
        string += f"cards left in shoe: {len(self.shoe.deck)}\n"
        string += f"decks left: {round(self.shoe.get_decks_left(), 2)}"

        return string

    # example
    # list_of_ids_and_stack_sizes = [(0, 5000), (87, 10000), (2, 4000)]
    @staticmethod
    def create_player_list(list_of_ids_and_stack_sizes):
        list = []
        for tuple in list_of_ids_and_stack_sizes:
            list.append(Player(tuple[0], tuple[1]))
        return list

    # overwrites player index, be careful
    def take_seat(self, index, player):
        if index < 0 or index > 6:
            raise InvalidSeat(f" please insert a seat position between 0 and 6, you gave: {index}")
        self.player_list[index] = player

    def replace_shoe(self, num_decks, deck_pen):
        self.num_decks = num_decks
        self.deck_pen = deck_pen
        self.shoe = Shoe(num_decks, deck_pen)


# add_player(0, 5000)
# add_player(1, 8000)
# add_player(2, 9000)
# dealer = Dealer()
#
# dealer.hand.add_card(shoe.deal_one())
# dealer.hand.add_card(shoe.deal_one())
# list_of_players[0].hand.add_card(shoe.deal_one())
# list_of_players[0].hand.add_card(shoe.deal_one())
# list_of_players[1].hand.add_card(shoe.deal_one())
# list_of_players[1].hand.add_card(shoe.deal_one())
# list_of_players[2].hand.add_card(shoe.deal_one())
# list_of_players[2].hand.add_card(shoe.deal_one())
#
# list_of_players[0].do_turn(dealer.hand.hand[0].card_face)
# list_of_players[1].do_turn(dealer.hand.hand[0].card_face)
# list_of_players[2].do_turn(dealer.hand.hand[0].card_face)
