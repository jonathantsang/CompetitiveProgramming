import sys

score = 0
cards = list(sys.stdin.readline().split()) # Rank,Suit

rvalue = { 'J': 10, 'Q': 10, 'K': 10}
for i in range(2, 11):
	rvalue[str(i)] = i

suits = {}
for card in cards:
	if card[1] in suits:
		suits[card[1]] += 1
	else:
		suits[card[1]] = 1

# initial
for card in cards:
	score += rvalue[card[0]]

# 1 at least 4 cards ad 1, product of J's and score in first card
if len(cards) >= 4:
	score += 1
numj = 0
for card in cards:
	if card[0] == 'J':
		numj += 1
score += ( numj * rvalue[cards[0][0]])

# 2 at least 2 cards of the same suit
for suit in suits:
	if suits[suit] >= 2:
		score *= 2
		break

# 3 at least one card of each suit
if len(suits) == 4:
	score *= 2

# 4
red = 0
black = 0