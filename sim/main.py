from blackjack_hi_low import Table
from player import Player
from dealer import Dealer

num_decks = 8
deck_pen = 0.75
min_bet = 10
max_bet = 1000

hands_per_hour = 100

game = Table(num_decks, deck_pen, min_bet, max_bet)
#
# init_players = [(0, 5000), (9, 10000), (2, 4000)]
# player_list = Table.create_player_list(init_players)
#
# i = 0
# for player in player_list:
#     game.take_seat(i, player)
#     i += 1
#
# game.take_seat(0, Player(6, 436))
# game.take_seat(1, Player(6, 543))

player = Player(69, 5000)
dealer = Dealer()

for i in range(200):
    player.receive_card(game.shoe.deal_one())
    player.receive_card(game.shoe.deal_one())

    game.dealer.receive_card(game.shoe.deal_one())
    game.dealer.receive_card(game.shoe.deal_one())

    hand_result = player.get_hand().get_hand_result(game.dealer.get_hand())
    print(f"dealer hand: {game.dealer.hand.get_hand_value()}")
    print(f"player hand: {player.hand.get_hand_value()}")
    print(hand_result)

    game.dealer.clear_hand()
    player.clear_hand()


print(game)
