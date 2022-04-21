import random
import time

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
            card['suit'] = suit
            card['face'] = get_card_face_from_value(value)
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
#Everything Above is from Dr. Laurence Liss , Intro to Python - Poker Lab, Temple University
#Everything below is from Daniel Hedberg and Aaron McDevitt for Dr. Andrew Rosen's Intro to Python Final Project

def fullDeck():
    deck1 = build_deck()
    deck2 = build_deck()
    deck3 = build_deck()
    deck4 = build_deck()
    deck5 = build_deck()
    deck6 = build_deck()
    fullDeck = (deck1+deck2+deck3+deck4+deck5+deck6)
    shuffle(fullDeck)
    return(fullDeck)


def OneGame(times, EndOfGame):
    countValues = {'2': 1,'3': 1,'4': 1,'5': 1,'6': 1,'7': 0,'8': 0,'9': 0,'10': -1, 'J': -1,'Q': -1,'K': -1,'A': -1}
    Deck = fullDeck()
    count = 0
    cards = 0
    NoAdvantage = 0
    _50 = 0
    _51 = 0
    _52 = 0
    GreaterThan53Advantage = 0
    for card in Deck:
        face = card['face']
        count += countValues[face]
        cards += 1
        decks_played = cards/52.0
        if (6 - decks_played) == 0:
            GameNumber = EndOfGame -times + 1
            print("End of Game " + str(GameNumber))
            return NoAdvantage, _50, _51, _52, GreaterThan53Advantage
        true_count = count / (6 - decks_played)

#Drawing Part

        if true_count < 1:
            NoAdvantage += 1
        elif 1 <= true_count <= 3:
            _50 += 1
        elif 3 < true_count <= 5:
            _51 += 1
        elif 5 < true_count <= 7:
            _52 += 1
        elif 7 < true_count:
            GreaterThan53Advantage += 1

def main():
    times = int(input("How many games should we analyze? "))
    EndOfGame = times #to keep track of "End of Game" print in OneGame function
    number_of_cards = 6*52*times
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while times:
        NoAdvantage, _50, _51, _52, GreaterThan53Advantage = OneGame(times, EndOfGame)
        a += NoAdvantage
        b += _50
        c += _51
        d += _52
        e += GreaterThan53Advantage
        NoAdvantage = 0
        _50 = 0
        _51 = 0
        _52 = 0
        GreaterThan53Advantage = 0
        times = times - 1
    print("Advantage\tEstimated Probability")
    print("%s\t%.6f" %("No Advantage:", a/number_of_cards))
    print("%s\t%.6f" %("50% to 51% Advantage:", b/number_of_cards))
    print("%s\t%.6f" %("51% to 52% Advantage:", c/number_of_cards))
    print("%s\t%.6f" %("52% to 53% Advantage:", d/number_of_cards))
    print("%s\t%.6f" %("Greater than 53% Advantage:", e/number_of_cards))
    
#Timer
            
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    print('--- {} seconds ---'.format(end_time))
