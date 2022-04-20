def generateCompFile(file, bin_string):
    f = open(f'./output/{file}_comp.bin', 'w')
    f.write(bin_string)
    f.close()
    print(f'Compressed file for {file} successfully generated')