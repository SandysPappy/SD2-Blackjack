from blackjack_hi_low import Table
from player import Player
from dealer import Dealer
from card import Card
from hand import Hand

def profit_percent(begin_ammount, end_ammount):
    return ((end_ammount - begin_ammount) / end_ammount) * 100

def get_player_average_bankroll(player_list):
    avg = 0
    total = 0
    num_players = 0
    for player in player_list:
        if player:
            total += player.stack_size
            num_players += 1

    return total / len(player_list)

num_decks = 8
deck_pen = 0.75
min_bet = 10
max_bet = 1000

total_rounds_played = 100000
start_stack_size = 100000
betting_units = 25

game = Table(num_decks, deck_pen, min_bet, max_bet)
player_list = []

for i in range(7):
    player_list.append(Player(i, start_stack_size, betting_units))

for i in range(7):
    player_list[i].take_seat(i, game)

print(game)
game.play_n_rounds(total_rounds_played)
print(game)

avg_end_stack = get_player_average_bankroll(player_list)


print(f"\nAfter {total_rounds_played} rounds played\n")

print(f"Average stack is ${avg_end_stack}\n")
print(f"Which leads to an average change of {round(profit_percent(start_stack_size, avg_end_stack), 2)}%")
