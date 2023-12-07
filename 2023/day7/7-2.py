from collections import Counter

class Hand:
    def __init__(self,hand):
        self.values = sorted(list(Counter(hand.replace('J','')).values()))
        # Case where the hand is 'JJJJJ'
        if not self.values: self.values = [0]
        self.values[-1] += hand.count('J')
    def get_type(self):
        if self.values[-1] == 5:
            return 'five'
        elif self.values[-1] == 4:
            return 'four'
        elif self.values[-1] == 3 and self.values[-2] == 2:
            return 'full_house'
        elif self.values[-1] == 3:
            return 'three'
        elif self.values[-1] == 2 and self.values[-2] == 2:
            return 'twopair'
        elif self.values[-1] == 2:
            return 'pair'
        else:
            return 'none'

# READ HANDS AND CLASSIFY THEM

hands = {
    'five': [],
    'four': [],
    'full_house': [],
    'three': [],
    'twopair': [],
    'pair': [],
    'none': []
}

with open('7.txt') as f:
    for line in f:
        hand_string, bet = line.strip('\n').split(' ')
        hand = Hand(hand_string)
        hands[hand.get_type()].append((hand_string,bet))

# SORT EACH HAND INSIDE EACH TYPE WITH A CUSTOM ORDER

cards = ['A','K','Q','J','T','9','8','7','6','5','4','3','2','J']
custom_order = dict(zip(cards,list(range(1,len(cards)+1))))
sorted_hands = []
for hands_list in hands.values():
    hands_list.sort(key=lambda x: [custom_order[char] for char in x[0]])
    sorted_hands += hands_list

# COMPUTE THE TOTAL RANK * BET

total = 0
for i,hand in enumerate(sorted_hands[::-1]):
    total += (i+1)* int(hand[1])
print(total)
