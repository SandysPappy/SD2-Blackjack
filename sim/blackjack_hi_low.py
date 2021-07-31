from shoe import Shoe
from hand import Hand
from card import Card
from player import Player
from dealer import Dealer
from math import floor
import basic_strategy as bs
import count_map as cm


# we're forcing players to only bet on one spot
class Table:
    def __init__(self, num_decks, deck_pen, min_bet, max_bet):
        self.num_decks = num_decks
        self.deck_pen = deck_pen
        self.shoe = Shoe(num_decks, deck_pen)

        self.player_list = [None] * 7
        self.dealer = Dealer()

        self.running_count = 0
        self.true_count = 0
        self.strategy = bs.get_basic_strategy()
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.count_map = cm.get_hi_low_map()

    def __str__(self):
        string = "Game state\n"

        string += f"min bet is {self.min_bet}\n"
        string += f"max bet is {self.max_bet}\n"
        string += "\n"

        string += f"Running count: {self.running_count}\n"
        string += f"True count: {self.true_count}\n"
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

    def deal_card(self, player):
        curr_card = self.shoe.deal_one()
        self.running_count += self.count_map[curr_card.card_face]
        self.true_count = floor(self.running_count / self.shoe.get_decks_left())

        if isinstance(player, Player):
            player.receive_card(curr_card)

        if isinstance(player, Dealer):
            player.receive_card(curr_card)

    def deal_inital_round(self):
        self.clear_table()
        for i in range(2):
            for player in self.player_list:
                if player is None:
                    continue
                self.deal_card(player)
            self.deal_card(self.dealer)

    def clear_table(self):
        if self.shoe.cut_card_reached:
            self.replace_shoe(self.num_decks, self.deck_pen)
        for player in self. player_list:
            if player is None:
                continue
            player.clear_hand()
            player.clear_bet()
        self.dealer.clear_hand()




    # example
    # list_of_ids_and_stack_sizes = [(0, 5000), (87, 10000), (2, 4000)]
    @staticmethod
    def create_player_list(list_of_ids_and_stack_sizes):
        list = []
        for tuple in list_of_ids_and_stack_sizes:
            list.append(Player(tuple[0], tuple[1]))
        return list

    def replace_shoe(self, num_decks, deck_pen):
        self.num_decks = num_decks
        self.deck_pen = deck_pen
        self.shoe = Shoe(num_decks, deck_pen)

    def play_turn(self, player):
        bs = basic_strategy.get_basic_strategy()

        curr_hand = self.hand.get_hand_value()
        hand_type = curr_hand[0]
        hand_value = curr_hand[1]

        action = bs[hand_type][(hand_value, up_card_face)]

        print(f"With a {curr_hand} and a dealer upcard of {up_card_face}, player {self._id} should {action}")


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
