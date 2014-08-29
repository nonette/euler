# Calculate the 3 most probable squares to land on in a Monopoly game with
# 4-sided dice.
#
# Just running the simulation

import collections
import logging
import random

squares = """go a1 cc1 a2 t1 r1 b1 ch1 b2 b3 jail c1 u1 c2 c3 r2 d1 cc2 d2 d3 fp
e1 ch2 e2 e3 r3 f1 f2 u2 f3 g2j g1 g2 cc3 g3 r4 ch3 h1 t2 h2""".split()

cc = 'go jail'.split() + ['x']*14
ch = 'go jail c1 e3 h2 r1 nextr nextu back3'.split() + ['x']*6

def p084(rounds=10**6, N=4):
    counts = collections.defaultdict(int)

    random.shuffle(ch)
    ch_ptr = 0
    random.shuffle(cc)
    cc_ptr = 0
    cur_square = 0
    doubles = 0
    for n in range(rounds):
        d1,d2 = random.randrange(1,N+1),random.randrange(1,N+1)
        if d1 == d2:
            doubles += 1
        else:
            doubles = 0
        if doubles == 3:
            doubles = 0
            cur_square = squares.index('jail')
        else:
            cur_square = (cur_square + d1 + d2) % len(squares)
        while True:
            val = squares[cur_square]
            if val == 'g2j':
                cur_square = squares.index('jail')
            elif val[:2] == 'ch':
                val = ch[ch_ptr]
                ch_ptr = (ch_ptr+1) % len(ch)
                if val in 'go jail c1 e3 h2 r1'.split():
                    cur_square = squares.index(val)
                elif val == 'nextr':
                    while squares[cur_square][0] != 'r':
                        cur_square = (cur_square+1) % len(squares)
                elif val == 'nextu':
                    while squares[cur_square][0] != 'u':
                        cur_square = (cur_square+1) % len(squares)
                elif val == 'back3':
                    cur_square = (cur_square-3) % len(squares)
                    continue
            elif val[:2] == 'cc':
                val = cc[cc_ptr]
                cc_ptr = (cc_ptr+1) % len(cc)
                if val in 'go jail'.split():
                    cur_square = squares.index(val)
            break
        counts[cur_square] += 1
    sortsquares = sorted([(v,k) for k,v in counts.items()])
    sortsquares = [(k,100.0*v/rounds) for v,k in sortsquares][::-1]
    logging.debug(sortsquares)
    return ''.join([str(k).zfill(2) for k,v in sortsquares[:3]])
    
