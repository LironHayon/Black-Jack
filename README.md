# Black-Jack

Black Jack is a popular casino game played with a standard 52 card deck. A single player plays against the "dealer".

Basic rules: 
In the first part of the game, the player is dealt cards repeatedly until one of the following events happens:
1. The player's score (i.e. the sum of the values of the player's cards, explained below) reaches 21. In this case, the player wins immediately.
2. The player's score exceed 21. In this case, the player loses immediately.
3. The player decides to "stay", i.e. not take any more cards.

If the player has neither won or lost at this point, it is the dealer's turn to draw cards. The dealer keeps 
drawing cards until the sum of her card values is 17 or higher. Then she stops and the winner is determined as follows:
1. If the dealer's score reaches 21, she wins.
2. If the dealer's score exceeds 21, the player wins.
3. If the sum of the card values of the player and the dealer are equal, the game is a "push" and nobody wins.
4. Otherwise, the person with the highest score wins.

Note that the dealer's behavior is completely deterministic -- the dealer must take another card if their
value is less than 17 and must stay if the value exceeds 17 (unless the dealer has already lost by that
point).

Card values: The card deck consists of 52 cards. There are four "suits": spades (♠), hearts (♥),
diamonds (♦) and clubs (♣). For each suit, there are 13 cards with different ranks: 9 number cards with
the values 2-10, three "face" cards Jack ("J"), Queen("K"), and King ("K"), and an Ace card ("A"). 
In black jack, all face cards have the value 10.

The value of an Ace card is normally 11, unless this would result in a total score of more than 21. In that
case, the value of the Ace is 1. Note that this means that the value of the Ace card may change during
the game. Assume the player initially draws an Ace (value 11), then a 2 (so the total value becomes 13),
and then a Queen. This would bring the total value to 23, but at this point the value of the Ace changes
to 1, so the total value of the hand is actually only 1+2+10=13.

(a) Write the class Card , which represents a single playing card. The class should define two data
fields, suit and rank. Both should be strings and they should be initialized with the parameters passed
to the __init__(self, suit, value) method, so you can create new Cards in the following way.
some_card = Card('♠','A')
another_card = Card('♥','10')
Write a suitable __str__(self) method for your class that returns a single string representing the
card's suit and rank.

(b) Complete the class CardCollection, which represents a collection of cards. This is used for the
hand of the player and dealer, and also for the initial deck of playing cards. The class has a data field
self.cards that refers to a list of Card instances. The CardCollection class has the following methods:
- __init__(self) creates an empty deck.
- add_card(self, card) adds a new card to the deck, where the card is an instance of the Card class.
- draw_card(self) remove a card from the collection and return it. The return value should be an instance of class Card.
- make_deck(self) populate the collection with a fresh deck of 52 cards. The order of the cards should be shuffled.
- value(self) returns the total value of the cards in the collection according to the rules mentioned above. This is a bit tricky 
because of the rules for the Ace. Note that the collection may contain up to 4 Aces (one for each suit), but only at most one of them 
may be interpreted as value 11 (otherwise the total would immediately exceed 21).

(c) Outside the Card and CardCollection classes, Write a main() function that plays a single game of
Black Jack according to the rules specified above. First, get a new deck of cards by creating a new
CardCollection object and then calling the make_deck() method. To deal a card, call the draw_card()
method. Then add the resulting card to another CardCollection representing the player's hand. Call
the value() method to determine the value of the player's hand.. After each card, evaluate if the
player has won or lost and otherwise ask her if they want another card. If the player decides to "stay",
perform the dealer's turn as described above (continue to use the same deck, but use a new
CardCollection for the dealer's hand).
