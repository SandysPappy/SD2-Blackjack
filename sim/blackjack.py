from random import randrange

class InvalidCardInitalization(ValueError):
  pass

class InvalidDeckNumber(ValueError):
  pass

class Card:
    # Card('A', 's')
    # s -> spades, h -> hearts, c -> clubs, d -> diamonds
    # 2-10, J, Q, K, A
    # Card('C', 't') represents cut card because im lazy
    def __init__(self, card_face: str, suit: str):
        # still allows for any character to be initalized in a card
        if type(card_face) != str or type(suit) != str or len(card_face) > 2 or len(suit) != 1:
            raise InvalidCardInitalization(f"Please enter a valid card, you gave: {card_face}{suit}")
        self.card_face = card_face.upper()
        self.suit = suit.lower()

    def __str__(self):
        return f"{self.card_face}{self.suit}"

    def __repr__(self):
        return str(self)

class Shoe:
    # returns a shoe containing num_decks with the cut card at the index
    # represented by the float cut_card_placement. Typlically this is 0.75
    # at a real casino and 0.50 at an online casino.
    # Note: the float is exact, so if you want to mimic a semirandom
    # cut_card_placement of range 0.70-0.80, then you must generate your own
    # random float before calling this constructor
    def __init__(self, num_decks: int, cut_card_placement: float):
        if num_decks <= 0:
            raise InvalidDeckNumber(f"Please enter a valid number of decks, you gave: {num_decks}")
        Shoe.deck = Shoe.get_shuffled_shoe(num_decks)
        # need to add a cut card to the deck here
        index_of_cut_card = int(cut_card_placement * len(Shoe.deck))
        Shoe.deck.insert(index_of_cut_card, Card('C', 't'))

    def __str__(self):
        return str(Shoe.deck)

    def __repr__(self):
        return str(self)

    def deal_one(self):
        if len(self.deck) <= 0:
            return None
        return self.deck.pop()

    # This should never be touched again, sorry it's gross looking
    # Returns a list of 52 unique Cards in order
    @staticmethod
    def get_ordered_deck():
        return [
                Card('a', 's'), Card('k', 's'), Card('q', 's'), Card('j', 's'), Card('10', 's'), Card('9', 's'), Card('8', 's'), Card('7', 's'), Card('6', 's'), Card('5', 's'), Card('4', 's'), Card('3', 's'), Card('2', 's'),
                Card('a', 'c'), Card('k', 'c'), Card('q', 'c'), Card('j', 'c'), Card('10', 'c'), Card('9', 'c'), Card('8', 'c'), Card('7', 'c'), Card('6', 'c'), Card('5', 'c'), Card('4', 'c'), Card('3', 'c'), Card('2', 'c'),
                Card('a', 'd'), Card('k', 'd'), Card('q', 'd'), Card('j', 'd'), Card('10', 'd'), Card('9', 'd'), Card('8', 'd'), Card('7', 'd'), Card('6', 'd'), Card('5', 'd'), Card('4', 'd'), Card('3', 'd'), Card('2', 'd'),
                Card('a', 'h'), Card('k', 'h'), Card('q', 'h'), Card('j', 'h'), Card('10', 'h'), Card('9', 'h'), Card('8', 'h'), Card('7', 'h'), Card('6', 'h'), Card('5', 'h'), Card('4', 'h'), Card('3', 'h'), Card('2', 'h'),
        ]

    # returns a new shuffled shoe without a cut card of deck len num_decks

    @staticmethod
    def random_insert(lst, item):
        lst.insert(randrange(len(lst)+1), item)

    @staticmethod
    def get_shuffled_shoe(num_decks: int):
        deck = []

        for i in range(num_decks):
            for card in Shoe.get_ordered_deck():
                deck.append(card)

        # need each card to be uniquely identifiable to shuffle them correctly
        deck_with_UIDs = []
        uid = 0
        for card in deck:
            deck_with_UIDs.append((uid, card))
            uid+=1

        # now to shuffle the cards

        # To shuffle the decks, we look at the bottom card of the deck
        # and memorize it. Take the top card of the deck and look at it. Is
        # that card the card that was originally on the bottom? No?
        # Put it into the deck randomly.
        # Repeat until you find the original bottom card.
        # Then, place that card into the deck randomly.
        # BAM you got a shuffled deck.

        # note: Python's random method seeds based on system time

        bottomCard = deck_with_UIDs[0]
        topCard = deck_with_UIDs.pop()

        # stops when we reach the memorized bottom card
        while topCard != bottomCard:
            Shoe.random_insert(deck_with_UIDs, topCard)
            topCard = deck_with_UIDs.pop()
        # topCard == bottomCard, so insert it back into the deck
        Shoe.random_insert(deck_with_UIDs, topCard)

        # removing uids since the deck is now shuffled
        shoe_with_uids_removed = [card[1] for card in deck_with_UIDs]
        return shoe_with_uids_removed

# print(len(Shoe.get_shuffled_shoe(8)))
# print(Shoe.get_shuffled_shoe(8))

test = Shoe(8, .99)
print(len(test.deck))
print(test.deal_one())
print(len(test.deck))
# print(test)
