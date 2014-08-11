## Count the number of hands the first player wins in the included file

from collections import Counter

filename = 'p054poker.txt'

cardvals = dict((val,i+2) for i,val in enumerate('23456789TJQKA'))
handvals = dict((val,i) for i,val in enumerate((
    'highcard',
    'onepair',
    'twopair',
    'threeofakind',
    'straight',
    'flush',
    'fullhouse',
    'fourofakind',
    'straightflush')))

# arrange cards first by frequency, then by value
def unclump(clumpedcards):
    clumpedcards.append(('', -1)) #dummy to mark end
    unclumpedcards = []
    curcount = 0
    curvals = []
    for val, count in clumpedcards:
        if count == curcount:
            curvals.append(val)
        else:
            curvals = sorted(curvals)[::-1]
            for v in curvals:
                unclumpedcards += [v]*curcount
            curvals = [val]
            curcount = count
    return unclumpedcards


# Return an array representing the value of the hand
# [handvalue, *cards by frequency then value]
# hand goodness will correspond to lexicographic ordering
def eval(hand):
    cards = (cardvals[c[0]] for c in hand)
    clumpedcards = Counter(cards).most_common()
    cards = unclump(clumpedcards)

    flush = (len(set(c[1] for c in hand)) == 1)
    straight = (cards == [cards[0]-i for i in range(len(cards))])

    handtype = ''
    if straight and flush:
        handtype = 'straightflush'
    elif clumpedcards[0][1] == 4:
        handtype = 'fourofakind'
    elif clumpedcards[0][1] == 3 and clumpedcards[1][1] == 2:
        handtype = 'fullhouse'
    elif flush:
        handtype = 'flush'
    elif straight:
        handtype = 'straight'
    elif clumpedcards[0][1] == 3:
        handtype = 'threeofakind'
    elif clumpedcards[0][1] == 2 and clumpedcards[1][1] == 2:
        handtype = 'twopair'
    elif clumpedcards[0][1] == 2:
        handtype = 'onepair'
    else:
        handtype = 'highcard'
    return [handvals[handtype]] + cards

def p054():
    with  open(filename) as f:
        hands = f.read()
    hands = hands.split()
    player1 = [hands[10*i:10*i+5] for i in range(len(hands)/10)]
    player2 = [hands[10*i+5:10*i+10] for i in range(len(hands)/10)]
    return sum(eval(player1[i]) > eval(player2[i]) for i in range(len(player1)))
