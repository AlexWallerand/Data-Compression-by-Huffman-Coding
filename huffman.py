"""Contains all the functions related to the Huffman tree and to calculate the binary string"""
#Imports the modules
from operator import attrgetter
from os import path

def count_occurences(text):
    """
    Returns a dictionnary associating a character with its frequency in the text string

    Parameters
    ----------
    text : str
        The text of the file

    Returns
    -------
    d : dict
        The dictionnary of frequencies
    """
    d = {}
    for char in text:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    d = dict(sorted(d.items(), key = lambda x: (x[1], x[0])))
    return d

class Node:
    """
    Node class used to build the tree
    """

    def __init__(self, label, frequency, leftChild = None, rightChild = None):
        """
        Constructor of the node class

        Parameters
        ----------
        label : str
            A character
        frequency: int
            The frequency associated to the character
        leftChild : Node object
            The left child of the node
        rightChild : Node object
            The right child of the node
        """
        self.label = label
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.edge = ''
        
    def getFrequency(self):
        """
        Method to get the frequency of the node

        No parameters
        """
        return self.frequency

    def setEdge(self, value):
        """
        Method to set the value of the rising edge of a node

        Parameters
        ----------
        value : int
            The value to set for the attribute
        """
        self.edge = value

    def __str__(self):
        """
        Override of the str method to print a node, only used to test

        No parameters
        """
        return f'{self.label} {self.edge} [{self.leftChild},{self.rightChild}]'

def build_huffman_tree(char_dict):
    """
    Returns the Huffman tree of the frequency dictionnary passed in parameter

    Parameters
    ----------
    char_dict : dict
        The dictionnary of characters with their frequencies
    
    Returns
    -------
    huffmanTree : list[node object]
        A list containig only one node object which is the Huffman tree
    """
    nodes = []

    for char in char_dict:
        nodes.append(Node(char, char_dict[char]))

    while len(nodes) > 1:
        nodes.sort(key = attrgetter('frequency','label'))

        left = nodes[0]
        left.setEdge('0')

        right = nodes[1]
        right.setEdge('1')

        sum = left.getFrequency() + right.getFrequency()
        node = Node(str(sum), sum, left, right)
        
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(node)
    
    huffmanTree = nodes
    return huffmanTree

def calculateCodes(node, value, code_dict):
    """
    Returns a dictionnary in which every character is associated with its binary string,
    by doing an in-depth course of the Huffman tree

    Parameters
    ----------
    node : Node object
        The node to check if it is a leaf or not
    value : str
        A binary string containing 0 or 1
    code_dict : dict
        The dictionnary in which the results are stored
    
    Returns
    -------
    code_dict : dict
        The dictionnary with the binary strings for every character
    """
    newValue = value + node.edge

    if node.leftChild != None:
        calculateCodes(node.leftChild, newValue, code_dict)
    if node.rightChild != None:
        calculateCodes(node.rightChild, newValue, code_dict)
    
    if node.leftChild == None and node.rightChild == None:
        code_dict[node.label] = newValue
    
    return code_dict

def calculateCompressRate(file_name):
    """
    Returns the compress rate, by getting the sizes of both the original and final files

    Parameters
    ----------
    file_name : str
        The name of the file to search
    
    Returns
    -------
    rate : float
        The rate in %
    """
    initial = path.getsize(file_name)
    file_name = file_name.removeprefix('./input/').removesuffix('.txt')
    file_name = f'./output/{file_name}_comp.bin'
    final = path.getsize(file_name)
    rate = 1 - (final/initial)
    rate = round(rate, 4)
    rate *= 100
    return rate

def calculateAverageBits(code_dict):
    """
    Returns the average number of bits per character, by getting the length of every binary strings

    Parameters
    ----------
    code_dict : dict
        The dictionnary in which the results are stored
    
    Returns
    -------
    res : float
        The average
    """
    values = code_dict.values()
    res = 0
    for value in values:
        res += len(value)
    res /= len(values)
    res = round(res, 3)
    return res