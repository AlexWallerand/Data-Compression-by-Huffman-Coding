"""Main file to execeute the compressions of the files in the input folder"""
#Imports the modules and files
from os import listdir
from os.path import isfile, join
from generateFreqFile import generateFreqFile
from generateCompFile import generateCompFile
from huffman import count_occurences, build_huffman_tree, calculateCodes, calculateAverageBits, calculateCompressRate

#Gets the files in the input folder and iterating on each of them to do the compression
files = [f for f in listdir('./input') if isfile(join('./input', f))]
for f in files:
    #Opens a file, read its content and calculate the dictionnary of frequencies
    file = open(f'./input/{f}', 'r')
    file_text = file.read()
    char_dict = count_occurences(file_text)
    #Builds the Huffman tree and calculate the binary strings by doing an in-depth course of it
    tree = build_huffman_tree(char_dict)
    codes = calculateCodes(tree[0], value = '', code_dict = {})
    #Iterates on the characters of the content of the file and adds into a binary string the bin code for each character
    bin_string = ''
    for char in file_text:
        bin_string += codes[char]
    #Converts the bin string into an integer in base 2
    bin = int(bin_string, base=2).to_bytes((len(bin_string) +7)//8, byteorder='big')
    #Generates the files and prints the results
    file_name = file.name.removeprefix('./input/').removesuffix('.txt')
    print(f'\nResults for {file_name} :')
    generateCompFile(file_name, bin)
    generateFreqFile(file_name, char_dict)
    print(f'Compress rate : {calculateCompressRate(file.name)}%')
    print(f'Average number of bits per character : {calculateAverageBits(codes)}')  