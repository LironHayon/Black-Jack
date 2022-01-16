#/usr/bin/python
# -*- coding: utf-8 -*-

import random

suits = ['♠','♣','♦','♥'] # Feel free to use these symbols to represent the different suits. 
ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
class Card(object):  
      
    #Two data fields, suit and rank. 
    #Both should be strings and they should be initialized with the parameters passed.
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    #returns a single string representing the card's suit and rank.
    def __str__(self):
        s = self.suit + self.rank 
        return s

class CardCollection(object): 

    #creates an empty deck. 
    def __init__(self):
        self.cards = []

    #adds a new card to the deck, where the card is an instance of the Card class.
    def add_card(self, card):
        self.cards.append(Card(card.suit, card.rank))

    #remove a card from the collection and return it. The return value should be an instance of class Card.
    def draw_card(self): 
        s = self.cards[len(self.cards)-1]
        self.cards.pop()
        return s

    #populate the collection with a fresh deck of 52 cards. The order of the cards should be shuffled.
    #The card deck consists of 52 cards. There are four "suits": spades (♠), hearts (♥), diamonds (♦) and clubs (♣). 
    #For each suit, there are 13 cards with different ranks: 9 number cards with the values 2-10, three "face" cards 
    #Jack ("J"), Queen("K"), and King ("K"), and an Ace card ("A"). In black jack, all face cards have the value 10. 
    def make_deck(self):
        for rank in ranks:   
            for suit in suits: 
                self.cards.append(Card(suit, rank))

        random.shuffle(self.cards)


        #self.cards = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣', 'A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥']
        
  

    #The value of an Ace card is normally 11, unless this would result in a total score of more than 21. In that case, the value of the Ace is 1. Note that this means that the value of the Ace card may change during the game. Assume the player initially draws an Ace (value 11), then a 2 (so the total value becomes 13), and then a Queen. This would bring the total value to 23, but at this point the value of the Ace changes to 1, so the total value of the hand is actually only 1+2+10=13.
    
    #returns the total value of the cards in the collection according to the rules mentioned above. This is a bit 
    #tricky because of the rules for the Ace. Note that the collection may contain up to 4 Aces (one for each suit)
    #but only at most one of them may be interpreted as value 11 (otherwise the total would immediately exceed 21).
    def value(self):
        sum = 0
        for card in self.cards:
            if card.rank == 'J' or card.rank == 'Q' or card.rank == 'K':
                sum += 10
            elif card.rank == "A":
                if sum > 10:
                    sum += 1
                else:
                    sum += 11
            else:
                sum += int(card.rank)
            
        return sum 
                


def main():
    deck = CardCollection()
    deck.make_deck() # initialize a fresh deck 
    player_hand = CardCollection()

    # complete the main method

    print("Let's play!")
    game = 'y'
    while (game == 'y'):
        print("You drew:")
        card = deck.draw_card()
        print(card)
        player_hand.add_card(card)
        print("Sum:", player_hand.value())
        
        #The player's score reaches 21 = the player wins immediately.
        if  player_hand.value() == 21:
            print("You win!")
            break

        #The player's score exceed 21 = the player loses immediately. 
        if player_hand.value() > 21:
            print("You exceeded 21, you lose.")
            break

        #The player decides to "stay", i.e. not take any more cards \ take more cards. 
        else:
            game = input("Do you want another card? (y/n): ")


    if player_hand.value() < 21 and player_hand.value() != 21:
        print("\nMy turn.")
        dealer_hand = CardCollection()

        while (dealer_hand.value() < 17):
            print("I drew:")
            card = deck.draw_card()
            print(card)
            dealer_hand.add_card(card)
            print("Sum:", dealer_hand.value())

        #If the dealer's score reaches 21, she wins.
        if dealer_hand.value() == 21:
            print("I win!")
            

        #If the dealer's score exceeds 21, the player wins.
        elif dealer_hand.value() > 21:
            print("I exceeded 21, you win!")
            
            
        #If the sum of the card values of the player and the dealer are equal, nobody wins. 
        elif dealer_hand.value() == player_hand.value():
            print("No one wins.")
            

        #Otherwise, the person with the highest score wins.
        else:
          if dealer_hand.value() > player_hand.value():
              print("I win!")
          else:
              print("You win!")



if __name__ == "__main__":
    main()
