class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)

        for card in hand:
            if counter[card]:
                for num in range(card, card + groupSize):
                    if counter[num]:
                        counter[num] -= 1
                    else:
                        return False
        
        return True

        