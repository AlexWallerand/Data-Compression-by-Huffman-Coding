from os import listdir
from os.path import isfile, join
from generateFreqFile import generateFreqFile
from generateCompFile import generateCompFile
from huffman import count_occurences, build_huffman_tree, calculateCodes, calculateAverageBits, calculateCompressRate

files = [f for f in listdir('./input') if isfile(join('./input', f))]
for f in files:
    file = open(f'./input/{f}', 'r')
    file_text = file.read()
    char_dict = count_occurences(file_text)
    tree = build_huffman_tree(char_dict)
    codes = calculateCodes(tree[0], value = '', code_dict = {})
    bin_string = ''
    for char in file_text:
        bin_string += codes[char]
    bin = int(bin_string, base=2).to_bytes((len(bin_string) +7)//8, byteorder='big')
    file_name = file.name.removeprefix('./input/').removesuffix('.txt')
    print(f'\nResults for {file_name} :')
    print(f'Compress rate : {calculateCompressRate(file.name)}%')
    print(f'Average number of bits per character : {calculateAverageBits(codes)}')
    generateCompFile(file_name, bin)
    generateFreqFile(file_name, char_dict)