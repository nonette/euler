## Decipher given text
# assume most common character is ' '
#

from collections import Counter
import itertools
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

def p059(filename = 'p059cipher1.txt', keylen = 3):
    with open(filename) as f:
        raw = f.read()
    code = [int(x) for x in raw.strip().split(',')]

    parts = [code[j::keylen] for j in range(keylen)]

    guess = [' ']*keylen
    for i, part in enumerate(parts):
        freqs = Counter(part).most_common()
        guess[i] = freqs[0][0]^ord(' ')
        parts[i] = [chr(x^guess[i]) for x in part]

    plaintext = ''.join(''.join(x) for x in itertools.izip_longest(*parts,
        fillvalue=''))
    logger.debug('key: %s' % ''.join(chr(x) for x in guess))
    logger.debug('plaintext: %s' % plaintext)

    return sum(ord(x) for x in plaintext)
