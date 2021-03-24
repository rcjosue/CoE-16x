def frequency_count(input_string):
     frequency = {}
     for letter in input_string:
          try:
              frequency[letter] = frequency[letter] + 1
          except KeyError:
               frequency[letter] = 1
     return frequency
print( frequency_count("CoE 161") )
