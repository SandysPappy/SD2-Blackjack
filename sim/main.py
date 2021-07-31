from blackjack_hi_low import Table
from player import Player

num_decks = 8
deck_pen = 0.75
hands_per_hour = 100

game = Table(num_decks, deck_pen, 10, 1000)

init_players = [(0, 5000), (9, 10000), (2, 4000)]
player_list = Table.create_player_list(init_players)

i = 0
for player in player_list:
    game.take_seat(i, player)
    i += 1

game.take_seat(0, Player(6, 436))
game.take_seat(1, Player(6, 543))

for i in range(300):
    game.shoe.deal_one()

print(game)
