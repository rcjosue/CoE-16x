import math
def uncompress(line):
    uncompressed = ''
    for letter in range( len(line) ):
        if (ord(line[letter]) > 47 and ord(line[letter]) < 58 ):
            x = (line[letter])
            letter += 1
            while( ord(line[letter]) > 47 and ord(line[letter]) < 58 ):
                x += (line[letter])
                letter += 1
            x = int(x) - 1
            uncompressed += x*(line[letter])
        else:
            uncompressed += (line[letter])
    return ( uncompressed )

def accurate_round(n):
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

T = int( input() )
for line in range (T):
    m = input()
    M = uncompress(m)
    c =  len(M)/len(m) 
    print(accurate_round(c), M)