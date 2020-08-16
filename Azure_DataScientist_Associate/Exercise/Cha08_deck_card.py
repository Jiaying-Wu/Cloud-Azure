# ranks and suits
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Spades", "Clubs", "Diamonds"]

# standard deck of cards
cards = []
for rank in ranks:
    for suit in suits:
        cards.append(rank + " of " + suit)
print(f"There are {len(cards)} cards in the deck.")

# Randomly choose five cards to add to a player's hand
print("Dealing ...")
import random
drafts = range(0, 5)

hand_cards = []
for draft in drafts:
    index = random.choice(range(0, 52 - draft))
    hand_cards.append(cards[index])
    cards.pop(index)

# check numbers of cards in hand
print(f"There are {len(cards)} cards in the deck.")

# print cards on hand
print(f"Player has the following cards in their hand:\n{hand_cards}")