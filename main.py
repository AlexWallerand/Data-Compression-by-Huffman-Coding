from os import listdir
from os.path import isfile, join
from generateFreqFile import generateFreqFile
from generateCompFile import generateCompFile
from huffman import count_occurences, build_huffman_tree, calculateCodes, calculateAverageBits, calculateCompressRate

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