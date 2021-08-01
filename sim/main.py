from blackjack_hi_low import Table
from player import Player
from dealer import Dealer
from card import Card
from hand import Hand

num_decks = 8
deck_pen = 0.75
min_bet = 10
max_bet = 1000
total_rounds_played = 10000

rounds_per_hour = 90

game = Table(num_decks, deck_pen, min_bet, max_bet)

def profit_percent(begin_ammount, end_ammount):
    return ((end_ammount - begin_ammount) / end_ammount) * 100

player1 = Player(1, 100000, 5)
player2 = Player(2, 100000, 5)
player3 = Player(3, 100000, 5)
player6 = Player(4, 100000, 5)

player1.take_seat(0, game)
player2.take_seat(5, game)
player3.take_seat(2, game)
player6.take_seat(3, game)

player1_original_stack = player1.stack_size
player2_original_stack = player2.stack_size
player3_original_stack = player3.stack_size
player6_original_stack = player6.stack_size

print(game)

game.play_n_rounds(total_rounds_played)

print(game)

print(f"After {total_rounds_played} rounds played")

print(f"Player1 started with {player1_original_stack} and ended with {player1.stack_size}")
print(f"Thats a change of {round(profit_percent(player1_original_stack, player1.stack_size), 2)}%")

print(f"Player2 started with {player2_original_stack} and ended with {player2.stack_size}")
print(f"Thats a change of {round(profit_percent(player2_original_stack, player2.stack_size), 2)}%")
