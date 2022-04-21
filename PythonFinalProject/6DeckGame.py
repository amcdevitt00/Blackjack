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

def graphicSetup():
    import tkinter
    import turtle
    t = turtle.Turtle()
    turtle.setup(225, 225)
    wn = turtle.Screen()
    wn.title("Hot Deck Meter")
    canvas = wn.getcanvas()
    wn.bgpic("images/meter.png")

    return (t, wn)
    
def main():
    (t, wn) = graphicSetup()
    countValues = {'2': 1,'3': 1,'4': 1,'5': 1,'6': 1,'7': 0,'8': 0,'9': 0,'10': -1, 'J': -1,'Q': -1,'K': -1,'A': -1}
    Deck = fullDeck()
    prob = dict()
    count = 0
    cards = 0
    for card in Deck:
        print(card)
        face = card['face']
        count += countValues[face]
        cards += 1
        decks_played = cards/52.0
        if (6 - decks_played) == 0:
            print("End of Game.")
            for i in prob:
                print("%s\t%.4f" %(i, prob[i]/cards))
            return prob
        true_count = count / (6 - decks_played)

#Drawing Part

        t.penup()
        if true_count < 1:
            t.color("blue")
            t.turtlesize(1)
            t.setx(-50)
            t.sety(-25)
            t.pendown
            turn = "No Advantage:"
            if turn in prob:
                prob[turn] += 1
            else:
                prob[turn] = 1
        elif 1 <= true_count <= 3:
            t.color("cyan")
            t.turtlesize(2)
            t.setx(-50)
            t.sety(-0)
            t.pendown
            turn = "50% to 51% Advantage:"
            if turn in prob:
                prob[turn] += 1
            else:
                prob[turn] = 1
        elif 3 < true_count <= 5:
            t.color("green")
            t.turtlesize(3)
            t.setx(-50)
            t.sety(25)
            t.pendown
            turn = "51% to 52% Advantage:"
            if turn in prob:
                prob[turn] += 1
            else:
                prob[turn] = 1            
        elif 5 < true_count <= 7:
            t.color("orange")
            t.turtlesize(4)
            t.setx(-50)
            t.sety(50)
            t.pendown
            turn = "52% to 53% Advantage:"
            if turn in prob:
                prob[turn] += 1
            else:
                prob[turn] = 1 
        elif 7 < true_count:
            t.color("red")
            t.turtlesize(5)
            t.setx(-50)
            t.sety(80)
            t.pendown
            turn = "Greater than 53% Advantage:"
            if turn in prob:
                prob[turn] += 1
            else:
                prob[turn] = 1  

#Timer
            
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time() - start_time
    print('--- {} seconds ---'.format(end_time))
