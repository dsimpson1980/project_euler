"""Poker hands
Problem 54
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives (see example 1
below). But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below); if the
highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD
        Pair of Fives       Pair of Eights      Player 2
2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH
        Highest card Ace    Highest card Queen  Player 1
3	 	2D 9C AS AH AC      3D 6D 7D TD QD
        Three Aces          Flush with Diamonds Player 2
4	 	4D 6S 9H QH QC      3D 6D 7H QD QS
        Pair of Queens      Pair of Queens
        Highest card Nine   Highest card Seven  Player 1
5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D
        Full House          Full House
        With Three Fours    with Three Threes   Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?"""

cards = {2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
         8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King',
         14: 'Ace'}

class Card(object):
    numerals = {str(n): n for n in range(2, 10)}
    numerals['T'], numerals['J'], numerals['Q'], numerals['K'] = range(10, 14)
    numerals['A'] = 14

    def __init__(self, rep):
        self._rep = rep
        self.numeral = self.numerals.get(rep[0], False)
        if not self.numeral:
            raise ValueError('Unrecognised numeral %s' % rep[0])
        if rep[1].upper() not in 'CSHD':
            raise ValueError('Unrecognised suit %s' % rep[1])
        self.suit = rep[1]

    def __repr__(self):
        return 'Card(%s)' % str(self._rep)


class Hand(object):
    def __init__(self, cards):
        self.cards = [c if isinstance(c, Card) else Card(c) for c in cards]
        self.suits = [card.suit for card in self.cards]
        self.flush = len(set(self.suits)) == 1
        self.numerals = sorted([card.numeral for card in self.cards])
        self.sets = {}
        for numeral in self.numerals:
            if numeral in self.sets:
                self.sets[numeral] += 1
            else:
                self.sets[numeral] = 1
        self.straight = self.numerals[4] - self.numerals[0] == 4 and len(self.sets) == 5
        self.value, self.hand = self._value()

    def __repr__(self):
        return 'Hand(%s)' % ' '.join([x._rep for x in self.cards])

    def _value(self):
        numerals = self.numerals
        if self.flush:
            # Flush or Straight flush
            if self.straight:
                if numerals[4] == 14:
                    hand = 'Royal Flush'
                else:
                    hand = 'Straight Flush %s High' % cards[numerals[4]]
                value = 9
            else:
                # Flush
                hand = 'Flush %s High' % cards[numerals[4]]
                value = 6
            return value + numerals[4] / 100.0, hand
        if self.straight:
            # Straight
            value = 5 + numerals[4] * 1e-2
            return value, 'Straight %s high' % cards[numerals[4]]
        if len(self.sets) == 2:
            # Full house or four of a kind
            hand = 'Full House %s over %s'
            for k, v in self.sets.iteritems():
                if v == 4:
                    value, value2, hand = 8, k, 'Four of a kind %ss' % cards[k]
                if v == 3:
                    value = 7
                if v == 2:
                    value2 = k
            return value + value2, hand
        if len(set(numerals)) == 3:
            # Three of a kind or Two pair
            if numerals[0] == numerals[2] or numerals[1] == numerals[3] or \
                            numerals[2] == numerals[4]:
                # three of a kind
                value = 4 + numerals[2] / 100.0
                hand = 'Three of a Kind %ss' % cards[numerals[2]]
                return value, hand
            # Two pair
            value2 = numerals[3] + numerals[1]/100
            high = [x for x in numerals if numerals.count(x) == 1][0]
            value = 3 + value2 / 100.0
            hand = 'Two Pair %ss and %ss %s high'
            hand %= tuple(cards[x] for x in [numerals[3], numerals[1], high])
            return value, hand
        if len(set(numerals)) == 4:
            # Pair
            value2 = [x for x in set(numerals) if numerals.count(x) > 1][0]
            high = numerals[2] if numerals[3] == numerals[4] else numerals[4]
            return 2 + value2 / 100.0, 'Pair of %ss, %s High' % (cards[value2],
                                                                 cards[high])
        # High card
        value2 = 0
        for n, x in enumerate(reversed(self.numerals), 1):
            value2 += x / 10.0 ** (2 * n)
        return 1 + value2, '%s High' % cards[self.numerals[4]]

count = 0
with open('data/poker.txt', 'r') as f:
    for n, line in enumerate(f):
        line = line.split(' ')
        hand1, hand2 = Hand(line[:5]), Hand(line[-5:])
        if hand1.value > hand2.value:
            count += 1
print 'Number of hands Player 1 wins = %s' % count
