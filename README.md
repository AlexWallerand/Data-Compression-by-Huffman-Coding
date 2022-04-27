# PROJ631_Huffman : Data compression by Huffman Coding

## Semi adaptive algorithm

In this project, the Huffman algorithm is used to compressed data, like in gzip files. It is based on a binary tree, build with the frequencies of every characters in a file. The tree is traversed to calculate the codes for each character. Every branch of the Tree as a value, 0 if it is a left child, 1 if it is a right child.

At the end of the program, the results are generated in two seperate files : the .bin file contains the compressed data in binary, and the .txt file containes the number of characters and their frequencies.
The compress rate and the average number of bits per character is also displayed in the terminal during the execution.

<p align = center>
<img width = 500 src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Huffman_tree_2.svg/1280px-Huffman_tree_2.svg.png"><br>
<i>Example of a Huffman Tree</i>
</p>

## Instructions for use

Drop in the input folder all the files you want to compress.<br>
Then, the program can be executed with the *main.py* file. Some information about the status of the compression and results are printed in the console. The resulted files can be found in the output folder.<br>
To execute the program, use a Python IDE, or enter this command in the console, in the directory of the project:
```
python main.py
```

## Analysis of the results

Here are the results printed by the terminal after the execution of the program for the three example files provided in the ouput folder :
```
Results for alice :
Compressed file for alice successfully generated
Frequency file for alice successfully generated
Compress rate : 44.41%
Average number of bits per character : 9.096

Results for extraitalice :
Compressed file for extraitalice successfully generated
Frequency file for extraitalice successfully generated
Compress rate : 45.190000000000005%
Average number of bits per character : 8.439

Results for textesimple :
Compressed file for textesimple successfully generated
Frequency file for textesimple successfully generated
Compress rate : 52.78%
Average number of bits per character : 4.188
```
<p align=center><i>Results printed in the terminal for the three files</i></p>

Firstly, we can see from these results that the average number of bits for a character increases with the size of the original file, since reading the results from bottom to top, we read by increasing file size. This is explained by the fact that the larger a file is, the more likely it is to contain a large number of different characters, and therefore a larger Huffman tree, and ultimately longer codes.
Then, the compression ratio is inversely proportional to the size of a file. However, this decrease in the compression rate seems to be less and less important as the size of a file increases.

There is a problem with the compression ratio, as it is based only on the binary code of the compressed file. However, for decompression purposes, the character frequency dictionary that must be provided in the binary file must be used. However, for our project, we have written this dictionary separately in another text file, which is not binary coded. Thus, if we want to calculate the actual compression ratio, taking into account the dictionary text file, the compression ratio becomes negative, because the text file is byte-encoded. 