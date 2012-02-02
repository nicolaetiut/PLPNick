"""Create an automated card dealer for a Texas Hold’em application.
It should be able to handle Deck objects, consisting of Cards.
Cards can be added or removed from Decks, and Decks can be shuffled
and sorted. When dealing cards, each Player receives a Hand
consisting of 2 Cards. After all cards are dealt, the Dealer should
draw the table Hand of 5 Cards
"""
import random


class Card:
    color = 'Blank'
    number = 'Blank'

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self):
        return self.number + " of " + self.color


class Deck:
    cards = []
    cards_sorted = []

    def __init__(self, colors, numbers):
        cards = []
        for number in numbers:
            for color in colors:
                card = Card(color, number)
                cards.append(card)
        self.cards = cards
        self.cards_sorted = cards
        self.shuffle()

    def insert_cards(self, cards):
        self.cards.extend(cards)

    def extract_cards(self, number):
        cards = []
        print "Dealing", number, "cards..."
        if len(self.cards) > number:
            for i in range(0, number):
                cards.append(self.cards.pop())
        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def reset_cards(self):
        self.cards = self.cards_sorted


class Player:
    hand = None
    name = 'Empty Slot'

    def __init__(self, name):
        self.name = name
        self.hand = Hand([])


class Hand:
    cards = []

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        result = ""
        for i in range(0, len(self.cards)):
            if i > 0 and i < len(self.cards):
                result += (", ")
            if i == len(self.cards):
                result += (" and ")
            result += str(self.cards[i])
        return result


class Poker_dealer:
    deck = None
    players = []
    max_players = 6
    table_hand = None

    def __init__(self, deck):
        self.deck = deck
        self.table_hand = Hand([])

    def add_player(self, player):
        if len(self.players) < self.max_players:
            self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def check_winner(self):
        print "Checking winner.."
        print "I have no idea"

    def run_game(self):
        if len(self.players) > 1:
            for player in self.players:
                hand = self.deck.extract_cards(2)
                player.hand.cards.extend(hand)
                print player.name, "received", player.hand
            hand = self.deck.extract_cards(5)
            self.table_hand.cards.extend(hand)
            print "Table received", self.table_hand
        else:
            print "Not enough players are present"

    def reset_game(self):
        for player in self.players:
            self.deck.insert_cards(player.hand.cards)
            self.deck.shuffle()
            player.hand.cards = []
        self.deck.insert_cards(self.table_hand.cards)
        self.table_hand.cards = []

if __name__ == "__main__":
    colors = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    numbers = ['Two', 'Three', 'Four', 'Five',
        'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Jack', 'Queen', 'King', 'Ace']
    dealer = Poker_dealer(Deck(colors, numbers))
    player1 = Player("Nick")
    player2 = Player("Tim")
    dealer.add_player(player1)
    dealer.add_player(player2)
    dealer.run_game()
    dealer.check_winner()
    dealer.reset_game()
