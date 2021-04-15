import re

def encoder_report(encoder, grimms_title, titles, lines):
    title_idx = titles.index(grimms_title)
    line_start = lines.index(grimms_title)
    line_end = lines.index(titles[title_idx + 1])

    orig_text = '\n'.join(lines[line_start:line_end])
    bitstring = huffman_encode(encoder, orig_text)

    return len(orig_text), len(bitstring)

class Node:
    def __init__(self, data, weight):
        self.left = None
        self.right = None
        self.data = data
        self.weight = weight

class HuffmanEncoder:
    def __init__(self, samples):
        alphabet = set(samples)
        alphabet_size = len(alphabet)

        nodes = [Node({symb}, samples.count(symb)) for symb in alphabet] #stores set in node.data and count in node.weight, set contains all letter that are part of the supernode

        for it in range(1, len(alphabet)):
            a,b = sorted(range(len(nodes)), key = lambda idx : nodes[idx].weight)[:2]
            
            supernode = Node(nodes[a].data.union(nodes[b].data), nodes[a].weight + nodes[b].weight)
            supernode.left = nodes[a]
            supernode.right = nodes[b]
            
            nodes = [nodes[idx] for idx in range(len(nodes)) if idx not in (a,b)]
            nodes.append(supernode)

        self.root = nodes[0]
    
    def encode(self, samples): #not sure how to use this, recursive?
        return huffman_encode(self, samples)

def huffman_encode(encoder, samples):
    ans = ''
    for letter in samples:
        curr_node = encoder.root
        while (curr_node.left!=None and curr_node.right!=None): #iterates through tree until leaf
            if letter in curr_node.left.data: #check if letter is in left or right set, moves current pointer and adds a 1 or 0 to ans
                curr_node = curr_node.left
                ans += '0'
            elif letter in curr_node.right.data:
                curr_node = curr_node.right
                ans += '1'
    return ans


if __name__ == '__main__':
    
    regex = re.compile("^( ){5}[A-Z',\\-\\[\\] ]+$")
    titles = []

    file_contents = open('grimms-fairy-tales.txt',encoding="utf8").read().replace('\r','')
    lines = file_contents.split('\n')
    
    for i in range(len(lines)):
        line = lines[i]
        if regex.match(line):
            titles.append(line[5:])
    titles.append('*****')

    encoder = HuffmanEncoder(list(file_contents))

    for grimms_title in titles[:-1]:
        print( grimms_title, encoder_report(encoder, grimms_title, titles, lines ))
    #grimms_title = titles[-6]
    #print( grimms_title, encoder_report(encoder, grimms_title, titles, lines ))
