from shoe import Shoe
from hand import Hand
from card import Card
from player import Player
from dealer import Dealer
import basic_strategy

bs = basic_strategy.get_basic_strategy()
running_count = 0
true_count = 0
hands_per_hour = 100

shoe = Shoe(8, 0.75)
list_of_players = []
list_of_hands = [None] * 7

cut_card_flag = False



def add_player(id, stack):
    list_of_players.append(Player(id, stack))

add_player(0, 5000)
add_player(1, 8000)
add_player(2, 9000)
dealer = Dealer()

dealer.hand.add_card(shoe.deal_one())
dealer.hand.add_card(shoe.deal_one())
list_of_players[0].hand.add_card(shoe.deal_one())
list_of_players[0].hand.add_card(shoe.deal_one())
list_of_players[1].hand.add_card(shoe.deal_one())
list_of_players[1].hand.add_card(shoe.deal_one())
list_of_players[2].hand.add_card(shoe.deal_one())
list_of_players[2].hand.add_card(shoe.deal_one())

list_of_players[0].do_turn(dealer.hand.hand[0].card_face)
list_of_players[1].do_turn(dealer.hand.hand[0].card_face)
list_of_players[2].do_turn(dealer.hand.hand[0].card_face)
