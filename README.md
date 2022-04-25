# PROJ631_Huffman : Data compression by Huffman Coding

## Semi adaptive algorithm

In this project, the Huffman algorithm is used to compressed data, like in gzip files. It is based on a binary tree, build with the frequencies of every characters in a file. The tree is traversed to calculate the codes for each character. Every branch of the Tree as a value, 0 if it is a left child, 1 if it is a right child.

At the end of the program, the results are generated in two seperate files : the .bin file contains the compressed data in binary, and the .txt file containes the number of characters and their frequencies.
The compress rate and the average number of bits per character is also displayed in the terminal during the execution.

<p align = center>
<img width = 500 src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Huffman_tree_2.svg/1280px-Huffman_tree_2.svg.png"><br>
<i>Example of a Huffman Tree</i>
</p>

## Program's architecture

This program has been developed completely in Python. As a consequence, it is not that complex technically. The *huffman.py* file contains all the functions that are used to build the Tree and calculate the codes.<br>
The Tree is built with a list of nodes, that are instances of the Node class. Every node is labeled with a character and its frequency, has a left (resp. right) child initialized at None, and every branch has a value (0 or 1).<br>

```
class Node:

    def __init__(self, label, frequency, leftChild = None, rightChild = None):
        self.label = label
        self.frequency = frequency
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.edge = ''
```
<p align = center><i>The constructor of the Node class</i><p>

The next step is to build the Tree. The function for this feature needs as a parameter, a dictionary whose keys and values are the characters and their frequencies respectively. This dictionnary is easily created by reading the file to compress, and by couting the occurences of every character. It is finally ordered by frequency and ASCII coding ascending.<br>
Then with the lists of nodes created with Node class, the tree is built following this algortihm:
```
Create a tree (leaf) for each character of the alphabet with the associated frequency
Repeat
Determine the 2 trees t1 and t2 of minimum frequency with t1.freq t2.freq
Create a new tree t with t1 and t2 as left and right subtrees respectively
with t.freq = t1.freq t2.freq
Until there is only one tree left
```
<p align = center><i>Algorithm to build the Huffman Tree</i><p>
Finally, it is already the last major phase of the compression. To calculate the binary codes of every character, the program has to go through all the tree and look at the values on the branches.
To do this, we use a recursive call of the function that calculates code. At each call, it verifies if there is at least one child to traverse (left or right). If it is not the case, the node is a leaf and the code has been appended with a 0 or a 1 at each call.
```
def calculateCodes(node, value = '', code_dict = {}):
    newValue = value + node.edge

    if node.leftChild != None:
        calculateCodes(node.leftChild, newValue, code_dict)
    if node.rightChild != None:
        calculateCodes(node.rightChild, newValue, code_dict)
    
    if node.leftChild == None and node.rightChild == None:
        code_dict[node.label] = newValue
    
    return code_dict

<p align = center><i>Function that goes through the Tree and calculates every codes</i><p>
The result is stored in a dictionnary with a key:value pair which is character:code.

Now that the coding has been made, we just need to generate the results.
There are two files to handle this :
<ul>
    <li>generateCompFile.py is used to produce the binary file. It contains a function that reads the original document and concatenate every character with its respective code.</li>
    <li>generateFreqFile.py is used to produce a text file showing the number of chracters and their frequencies in the original file. It just writes into a file the data in the first dictionnary we calculated above.</li>
</ul>
Both files are produced in the output folder.

The program can be executed with *main.py*. It contains instructions that search for all the files in the input folder. Then, for each file, it calculates the occurences of every character, build the corresponding Huffman Tree, traverse it to calculate the codes, and finally generates the results.
Moreover, it prints in the console the compress rate of the operation, and the average number of bits per character.

```
files = [f for f in listdir('./input') if isfile(join('./input', f))]
for f in files:
    file = open(f'./input/{f}', 'r')
    text = file.read()
    dict = count_occurences(text)
    tree = build_huffman_tree(dict)
    codes = calculateCodes(tree[0])
    res = ""
    for char in text:
        res += codes[char]
    file_name = file.name.removeprefix('./input/').removesuffix('.txt')
    print(f'\nResults for {file_name} :')
    print(f'Compress rate : {calculateCompressRate(file.name, res)}')
    print(f'Average bits per character : {calculateAverageBits(codes)}')
    generateCompFile(file_name, res)
    generateFreqFile(file_name, dict)
```
<p align="center"><i>Code of the main.py executable</i></p>




