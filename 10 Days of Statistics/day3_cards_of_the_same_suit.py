"""
Task:
You draw 2 cards from a standard 52-card deck without replacing them.
What is the probability that both cards are of the same suit?

Ans:
12/51
"""

# Solve with code
from collections import Counter, namedtuple
from enum import Enum
from itertools import product, combinations

from sympy import symbols

Suit = Enum("Suit", "♡ ♢ ♤ ♧")
Rank = Enum("Rank", "A 2 3 4 5 6 7 8 9 10 J Q K")
Card = namedtuple("Card", "suit rank")
deck = [Card(suit, rank) for suit, rank in product(Suit, Rank)]
draws = list(combinations(deck, 2))  # draw 2 cards without replacement

n_matched, n_elements = symbols("n N")
probability = n_matched / n_elements

matches = list(filter(lambda card: card[0].suit == card[1].suit, draws))
rate = probability.subs({"n": len(matches), "N": len(draws)})

for n, N in [(1, 156), (12, 39), (1, 39), (12, 51)]:
    if rate == probability.subs({"n": n, "N": N}):
        print(f"option: {n}/{N}")
        print("rate:", rate)