import time
def algo (layers):
     ''' Control Algorithm'''
     pins = 0
     for i in range (1,layers):
         pins += i
     return (pins+layers)

def algo1 (layers):
     '''Algorithm 1, predefined list sum function'''
     pins = list(range(1,layers+1))
     return sum(pins)

def algo2 (layers):
     '''Algorithm 2, pattern with modulo and multiplication'''
     pins = int(layers/2)
     if (layers%2 ==1):
          return ( (pins+1) * layers )
     else:
          return (pins * layers + pins)

def algo3 (layers):
     '''Algorithm 3, pattern with bitwise operations'''
     pins = layers>>1
     if (layers & 1):
          return ( ( pins+1 ) * layers )
     else:
          return (pins * layers + pins)

''' EXTENDED PROFILING 
algo_times = [ [], [], [], [] ]
algos = [algo, algo1, algo2, algo3]
for repeat in range (3): #Repeats loops 3 times 
     for no in range (4): #Sets the number of algorithm to be used and appends the time for each run in respective list
          start_t = time.time()
          for i in range (1,401):
               print (algos[no](i))
          end_t = time.time()
          algo_times[no].append(end_t - start_t)
          
print ("Algorithm Profiling:")
for arr in algo_times:
     print( sum(arr)/3 )
     
print ("Raw Times:")
for i in range (4):
     print (algo_times[i])
'''     

''' INITIAL PROFILING
for i in range (1,401):
     #print (algo1(i) ) # 2.3515286445617676s , 2.2744452953338623s , 1.2495057582855225s , 1.217909336090088s , 1.3120441436767578s
     #print (algo2(i) ) # 2.1286933422088623s , 1.9764690399169922s , 1.2023749351501465s , 1.1398005485534668s, 1.3340716361999512s
     #print (algo3(i) ) # 2.2373850345611572s , 2.0924601554870605s, 1.1866683959960938s , 1.1554367542266846s, 1.3371469974517822s
     #print(algo4(i)) # 2.229813003540039s, 2.199257278442383s, 1.1554038524627686s, 1.1397933959960938s, 1.3234243392944336s
     print (algo1(i) , algo2(i) , algo3(i) , algo(i)) #Check for correctness

'''

inp = int(input("Input: "))
print ( "Output:", algo3(inp) )

