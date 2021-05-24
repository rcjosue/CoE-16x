import random
hand_cards = [random.randint(1, 13) for x in range(12)]
# Unsorted hand_cards
print(hand_cards)
for i in range(len(hand_cards)):
     '''sorts cards one at a time from left to right'''
     j = i
     while j > 0 and hand_cards[j] < hand_cards[j - 1]:
          hand_cards[j], hand_cards[j - 1] = \
          hand_cards[j - 1], hand_cards[j]
          j = j - 1
     #print(hand_cards)
# Sorted hand_cards
print(hand_cards)
