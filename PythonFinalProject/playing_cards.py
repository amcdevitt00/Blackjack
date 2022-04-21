import random

def get_card_color_from_suit(suit):
    if suit == 'Spades' or suit == 'Clubs':
        return 'black'
    else:
        return 'red'

def get_card_face_from_value(value):
    if value <= 10:
        return str(value)
    elif value == 11:
        return 'J'
    elif value == 12:
        return 'Q'
    elif value == 13:
        return 'K'
    else:
        return 'A'

def build_deck():
    deck = []
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = range(2, 15)
    for suit in suits:
        for value in values:
            card = {}
            card['suit'] = suit
            card['face'] = get_card_face_from_value(value)
            deck.append(card)

    return deck

def shuffle(deck):
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def main1():
    deck1 = build_deck()
    deck2 = build_deck()
    deck3 = build_deck()
    deck4 = build_deck()
    deck5 = build_deck()
    deck6 = build_deck()
    fullDeck = (deck1+deck2+deck3+deck4+deck5+deck6)
    shuffle(fullDeck)
    for card in fullDeck:
        print(card)
        

if __name__ == '__main__':
    main1()
