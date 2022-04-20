def alphabet_size(char_dict):
    return str(len(char_dict))

def generateFreqFile(file, char_dict):
    f = open(f'./output/{file}_freq.txt', 'w')
    f.write(f'Number of characters : {alphabet_size(char_dict)}\n')
    for char in char_dict:
        f.write(f'{char} : {str(char_dict[char])}\n')
    f.close()
    print(f'Frequency file for {file} successfully generated')
