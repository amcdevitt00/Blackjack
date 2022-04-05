# Blackjack
'''
module to create a shuffle a deck of cards.
'''

import random

def get_card_color_from_suit(suit):
    '''
    Given a string representing a card suit
    return the color of the card (red or black).
    '''
    if suit == 'Spades' or suit == 'Clubs':
        return 'black'
    else:
        return 'red'


def get_card_face_from_value(value):
    '''
    Given an integer representing a card value
    return the card face (2 through A).
    '''
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
    '''
    Create a list representing a deck of cards. Each
    item in the list is a dictionary representing a single card.
    '''
    deck = []
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    values = range(2, 15)
    for suit in suits:
        for value in values:
            card = {}
            card['value'] = value
            card['suit'] = suit
            card['face'] = get_card_face_from_value(value)
            card['color'] = get_card_color_from_suit(suit)
            deck.append(card)

    return deck


def shuffle(deck):
    '''
    Implement the Fischer-Yates Shuffle to shuffle the cards.
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    '''
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        temp = deck[j]
        deck[j] = deck[i]
        deck[i] = temp


def fullDeck():
    deck1 = build_deck()
    deck2 = build_deck()
    deck3 = build_deck()
    deck4 = build_deck()
    deck5 = build_deck()
    deck6 = build_deck()
    fullDeck = (deck1)
    shuffle(fullDeck)
    for card in fullDeck:
        return(card)
    
        

CARD_VALUES = {
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1,
        '7': 0,
        '8': 0,
        '9': 0,
        '10': -1, 
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1,
        }

DECKS = 1

def main():
    count = 0
    cards = 0
    _input = True
    decks_played = 0
    while _input:
        element = fullDeck()
        print(element)
        _input = element['face']
        cards += len(_input)
        count += CARD_VALUES[_input]
        decks_played = cards / 52.0
        true_count = count / (DECKS - decks_played)
        print('Count: {}'.format(count))
        print('True Count: {}'.format(true_count))
    print('Decks played: {}'.format(decks_played))

if __name__ == '__main__':
    main()
