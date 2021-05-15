def frequency_count(input_string):
     frequency = {}
     for letter in input_string:
          frequency[letter] = frequency.get( letter, 0 ) + 1
     return frequency
print( frequency_count("CoE 161") )
