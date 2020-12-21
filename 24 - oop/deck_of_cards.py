import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit_list = ["Hearts", "Spades", "Clubs", "Diamonds"]

    def __init__(self):
        self.deck_list = [Card(value, suit) for value in Deck.value_list for suit in Deck.suit_list]

        # below taken from stackoverflow list of lists flattening
        # didn't need to use it though, as I changed approach
        # self.deck_list = [item for sublist in self.deck_list for item in sublist]
        print(self.deck_list)

    def __repr__(self):
        return f"Deck of {self.count_cards()} cards"

    def count_cards(self):
        return len(self.deck_list)

    def shuffle(self):
        if self.count_cards() < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            random.shuffle(self.deck_list)
            return self.deck_list

    def _deal(self, deal_num):
        self.deal_num = deal_num
        self.pop_deck = []

        if self.count_cards() == 0:
            raise ValueError("All cards have been dealt")
        elif deal_num > self.count_cards():
            return self._deal(self.count_cards())
        else:
            for i in range(self.deal_num):
                self.pop_deck.append(self.deck_list.pop(-1))
            return self.pop_deck

    def deal_card(self):
        return f"deal card: {self._deal(1)[0]}"

    def deal_hand(self, hand_size):
        return f"deal hand: {self._deal(hand_size)}"


# instantiation
d = Deck()
print(d.count_cards())
print(d.shuffle())
d.deal_card()
print(d.count_cards())
d.deal_hand(5)
print(d.count_cards())
d.deal_hand(47)
print(d.count_cards())
