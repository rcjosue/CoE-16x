class Node:
    def __init__(self, symbol=None):
        self.left = None
        self.right = None
        self.data = symbol

    def __del__(self):
        if self.left is not None:
            del self.left
        if self.right is not None:
            del self.right
        del self.data
    
    def insert(self, bitstring, symbol):
        if bitstring == '':
            self.data = symbol
        elif bitstring[0] == '0':
            if self.left is None:
                self.left = Node()
            
            self.left.insert(bitstring[1:], symbol)
        elif bitstring[0] == '1':
            if self.right is None:
                self.right = Node()
            
            self.right.insert(bitstring[1:], symbol)

class Decoder:
    def __init__(self, symbol_map):
        self.root = Node()
        for (bit_string, symbol) in symbol_map.items():
            self.root.insert(bit_string, symbol)
    
    def __del__(self):
        del self.root


def prefix_free_decode(decoder, bit_string): #take in Decoder(class) object and encoded string, returns decoded string
    ans = ''
    curr_node = decoder.root
    for bit in bit_string: #iterates through all bits in bit_string
        if bit == '0': #iterates through the binary tree based on the value of bit
            if curr_node.left == None: #adds symbol at node to answer if no node is connected to where the bit directs it
                ans += curr_node.data
                curr_node = decoder.root.left
            else:
                curr_node = curr_node.left
        elif bit == '1':
            if curr_node.right == None:
                ans += curr_node.data
                curr_node = decoder.root.right
            else:
                curr_node = curr_node.right
    ans += curr_node.data
    return ans


test_decoder = {'10010':'p', '10011':'t', '0100':'d', '1110':'i', '000':'n' , '10100':'y' , '0101': 'c', '10101':'u', '0110':'s', '10110':'h','0111':'r', '110':' ', '001': 'e', '10111':'v', '1111':'a' ,'1000':'g'}
#decoder = Decoder(test_decoder)
#decoder = Decoder({'00':'e','01':'h','10':'y', '11':' '})
decoder = Decoder({'0':'hey','1':' '})
print (prefix_free_decode(decoder,'01010' ) )



