"""Contains the functions to generate the frequency file"""
def alphabet_size(char_dict):
    """
    Get the number of characters in the dictionnary of frequencies

    Parameters
    ----------
    char_dict : dict
        The dictionnary of characters with their frequencies 
    
    Returns
    -------
    int
        The number of keys in the dictionnary
    """
    return str(len(char_dict))

def generateFreqFile(file_name, char_dict):
    """
    Generates the txt file that shows the number of characters, and their frequencies

    Parameters
    ----------
    file_name : str
        The name of the file
    char_dict : dict
        The dictionnary of characters with their frequencies
    
    Returns
    -------
    No return, prints that the frequency file has been generated
    """
    f = open(f'./output/{file_name}_freq.txt', 'w')
    f.write(f'{alphabet_size(char_dict)}\n')
    for char in char_dict:
        if char != '\n':
            f.write(f'{char} {str(char_dict[char])}\n')
        else:
            f.write(f'\\n {str(char_dict[char])}\n')
    f.close()
    print(f'Frequency file for {file_name} successfully generated')
