## Total letters needed to write 1..1000 longhand

digits = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine"} 

irregular = {10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}

british_and = "and"

places = {2: "hundred", 3: "thousand", 6: "million", 9: "billion", 
        12: "trillion"}


def spell_out(n):
    n = str(n)
    if len(n) == 0:
        return ""
    d = int(n[0])
    if len(n) == 1:
        return digits[d]
    elif len(n) == 2:
        if d == 1:
            return irregular[int(n)]
        if d > 1:
            return tens[d] + digits[int(n[1])]
    elif len(n) == 3:
        retval = ''
        retval += digits[d] + places[2]
        loworder = n[1:]
        if int(loworder) != 0:
            retval += british_and
            retval += spell_out(str(int(loworder)))
        return retval

    retval = ''
    highorder = n[:(len(n)%3 or 3)]
    loworder = n[(len(n)%3) or 3:]
    retval += spell_out(highorder)
    retval += places[len(loworder)]
    if 0 < int(loworder) < 100:
        retval += british_and
    retval += spell_out(str(int(loworder)))

    return retval            

def p017(N=1000):
    return sum(len(spell_out(str(n))) for n in range(1,N+1))
