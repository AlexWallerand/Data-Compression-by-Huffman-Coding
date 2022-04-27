"""Contains the function to generate the bin file"""
def generateCompFile(file_name, bin):
    """
    Generates the bin file, by writing an integer in base 2 in a file opened in wb mode

    Parameters
    ----------
    file_name : str
        The name of the file
    bin : int
        The integer of the text in base 2, to write in the file generated

    Returns
    -------
    No return, prints that the file has been generated
    """
    f = open(f'./output/{file_name}_comp.bin', 'wb')
    f.write(bin)
    f.close()
    print(f'Compressed file for {file_name} successfully generated')