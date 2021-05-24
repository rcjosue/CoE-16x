#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def uncompress(message):
    '''Takes a message with utf-8 characters and uncompresses it using the numbers in the message'''
    uncompressed = '' #initialize the uncompressed string
    message_length = len(message)
    letter = 0 # initializes iterator
    while letter < message_length:
        if ( (ord(message[letter]) > 47) and (ord(message[letter]) < 58) ): #checks if the current char is a number
            multiplier = str(message[letter])
            letter += 1
            while( (ord(message[letter]) > 47) and (ord(message[letter]) < 58) ):#checks if the next chars are numbers and adds then to a string
                multiplier += (message[letter])
                letter += 1
            multiplier = int(multiplier) # converts string of numbers into integer
            uncompressed += multiplier*(message[letter]) #appends the next non-number character x times
        else:
            uncompressed += (message[letter]) #append non-number characters to the uncompressed string
        letter += 1
    return ( uncompressed )

def get_ratio(len_M , len_m):
    '''Calculates compression ratio rounds off to the nearest integer'''
    r = len_M / len_m
    if (r - math.floor(r)) < 0.5: #checks if value in decimals place are < 0.5 and rounds down if true
        return math.floor(r) 
    return math.ceil(r) #rounds-up if decimal is 0.5 or greater

T = int( input() ) #number of messages to be read and uncompressed
for line in range ( T ):
    m = input() #takes in 1 line message, m
    M = uncompress( m ) #uncompressed message, M
    c = get_ratio( len(M), len(m) ) #compression ratio, c
    print( c, M )
