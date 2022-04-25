def generateCompFile(file, bin):
    f = open(f'./output/{file}_comp.bin', 'wb')
    f.write(bin)
    f.close()
    print(f'Compressed file for {file} successfully generated')