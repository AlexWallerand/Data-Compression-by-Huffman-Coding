from operator import itemgetter, attrgetter
from turtle import left

def count_occurences(text):
    dict = {}
    for char in text:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    dict = sorted(dict.items(), key = itemgetter(1))
    return dict

class Node:

    def __init__(self, label, frequency, leftChild = None, rightChild = None):
        self.label = label
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.edge = None
        
    def getFrequency(self):
        return self.frequency

    def setEdge(self, value):
        self.edge = value

    def __str__(self):
        return f'{self.label} [{self.leftChild},{self.rightChild}]'

def build_huffman_tree(char_dict):
    nodes = []

    for char in char_dict:
        nodes.append(Node(char, char_dict[char]))

    while(len(nodes)) > 1:
        nodes.sort(key = attrgetter('frequency'))

        left = nodes[0]
        left.setEdge(0)

        right = nodes[1]
        right.setEdge(1)

        sum = left.getFrequency() + right.getFrequency()
        node = Node(str(sum), sum, left, right)
        
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(node)
    
    HuffmanTree = nodes
    return HuffmanTree 
       
if __name__ == '__main__':
    build_huffman_tree({'B' : 1, 'D' : 3, 'A' : 5, 'C' : 6})

