"""
Five of a kind, where all five cards have the same label: AAAAA
Four of a kind, where four cards have the same label and one card has a different label: AA8AA
Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
High card, where all cards' labels are distinct: 23456
"""

import pandas as pd
import pandasql as ps

file = open('input.txt', 'r')
lines = file.readlines()
my_hands = []
CARD_VALUES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_SCORES = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
HAND_TYPES = {'Five of a kind': 7, 'Four of a kind': 6, 'Full house': 5, 'Three of a kind': 4, 'Two pair': 3, 'One pair': 2, 'High card': 1}


for line in lines:
    hand, bid = line.split()
    my_hands.append({"hand": hand, "bid": int(bid)})


def count_cards(hand):
    cards = {}
    for card in hand:
        cards[card] = 1 if card not in cards else cards[card] + 1
        # print(card)
    return cards

def label_hand(cards):
    counts = []
    for k, v in cards.items():
        if k in CARD_VALUES:
            counts.append(v)
    
    if max(counts)==5:
        return 'Five of a kind'
    elif max(counts)==4:
        return 'Four of a kind'
    elif max(counts)==3:
        if 2 in counts:
            return 'Full house'
        else:
            return 'Three of a kind'
    elif max(counts)==2 and counts.count(2)==2:
        return 'Two pair'
    elif max(counts)==2:
        return 'One pair'
    else:
        return 'High card'
    return 'Unknown'

def rank_hands(hands):
    for hand in hands:
        card_index = 5
        hand_score = 0
        print(hand)
        for card in hand['hand']:
            hand_score = hand_score + (CARD_SCORES[CARD_VALUES.index(card)]) * (14**(card_index-1))
            card_index -= 1
        hand['hand_score'] = hand_score + HAND_TYPES[hand['label']] * (14**5)
    return hands


def summarize_hands(h):
    df = pd.DataFrame(h)
    summary = ps.sqldf("select hand, label, bid, hand_score, rank() over(order by hand_score asc) as rnk from df order by hand_score desc")
    summary['total_score']= summary['rnk']*summary['bid']
    print(summary['total_score'].sum())
    # summary = ps.sqldf("select hand, label, hand_score from df order by hand_score desc")
    return summary
    

for hand in my_hands:
    hand.update(count_cards(hand["hand"]))
    hand['label'] = label_hand(hand)
    # print(hand)






my_hands = rank_hands(my_hands)
print(summarize_hands(my_hands))