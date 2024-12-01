import re
import numpy as np
from PIL import Image
print("Huffman Compression Program")
print("=================================================================")
h = int(input("Enter 1 if you want to input an colour image file, 2 for default gray scale case:"))
if h == 1:
    file = input("Enter the filename:")
    my_string = np.asarray(Image.open(file),np.uint8)
    shape = my_string.shape
    a = my_string
    print ("Entered string is:",my_string)
    my_string = str(my_string.tolist())
elif h == 2:
    array = np.arange(0, 737280, 1, np.uint8)
    my_string = np.reshape(array, (1024, 720))
    print ("Entered string is:",my_string)
    a = my_string
    my_string = str(my_string.tolist())
else:
    print("You entered invalid input")                    # taking user input

letters = []
only_letters = []
for letter in my_string:
    if letter not in letters:
        frequency = my_string.count(letter)             # frequency of each letter repetition
        letters.append(frequency)
        letters.append(letter)
        only_letters.append(letter)

nodes = []
while len(letters) > 0:
    nodes.append(letters[0:2])
    letters = letters[2:]                               # sorting according to frequency
nodes.sort()
huffman_tree = []
huffman_tree.append(nodes)                             # Make each unique character as a leaf node

def combine_nodes(nodes):
    pos = 0
    newnode = []
    if len(nodes) > 1:
        nodes.sort()
        nodes[pos].append("1")                       # assigning values 1 and 0
        nodes[pos+1].append("0")
        combined_node1 = (nodes[pos] [0] + nodes[pos+1] [0])
        combined_node2 = (nodes[pos] [1] + nodes[pos+1] [1])  # combining the nodes to generate pathways
        newnode.append(combined_node1)
        newnode.append(combined_node2)
        newnodes=[]
        newnodes.append(newnode)
        newnodes = newnodes + nodes[2:]
        nodes = newnodes
        huffman_tree.append(nodes)
        combine_nodes(nodes)
    return huffman_tree                                     # huffman tree generation

newnodes = combine_nodes(nodes)

huffman_tree.sort(reverse = True)
print("Huffman tree with merged pathways:")

checklist = []
for level in huffman_tree:
    for node in level:
        if node not in checklist:
            checklist.append(node)
        else:
            level.remove(node)
count = 0
for level in huffman_tree:
    print("Level", count,":",level)             #print huffman tree
    count+=1
print()

letter_binary = []
if len(only_letters) == 1:
    lettercode = [only_letters[0], "0"]
    letter_binary.append(letter_code*len(my_string))
else:
    for letter in only_letters:
        code =""
        for node in checklist:
            if len (node)>2 and letter in node[1]:           #genrating binary code
                code = code + node[2]
        lettercode =[letter,code]
        letter_binary.append(lettercode)
print(letter_binary)
print("Binary code generated:")
for letter in letter_binary:
    print(letter[0], letter[1])

bitstring =""
for character in my_string:
    for item in letter_binary:
        if character in item:
            bitstring = bitstring + item[1]
binary ="0b"+bitstring
print("Your message as binary is:")
                                        # binary code generated

uncompressed_file_size = len(my_string)*7
compressed_file_size = len(binary)-2
print("Your original file size was", uncompressed_file_size,"bits. The compressed size is:",compressed_file_size)
print("This is a saving of ",uncompressed_file_size-compressed_file_size,"bits")
output = open("compressed.txt","w+")
print("Compressed file generated as compressed.txt")
output = open("compressed.txt","w+")
print("Decoding.......")
output.write(bitstring)

bitstring = str(binary[2:])
uncompressed_string =""
code =""
for digit in bitstring:
    code = code+digit
    pos=0                                        #iterating and decoding
    for letter in letter_binary:
        if code ==letter[1]:
            uncompressed_string=uncompressed_string+letter_binary[pos] [0]
            code=""
        pos+=1

print("Your UNCOMPRESSED data is:")
if h == 1:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, shape)
    print(res)
    print("Observe the shapes and input and output arrays are matching or not")
    print("Input image dimensions:",shape)
    print("Output image dimensions:",res.shape)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    if a.all() == res.all():
        print("Success")
if h == 2:
    temp = re.findall(r'\d+', uncompressed_string)
    res = list(map(int, temp))
    print(res)
    res = np.array(res)
    res = res.astype(np.uint8)
    res = np.reshape(res, (1024, 720))
    print(res)
    data = Image.fromarray(res)
    data.save('uncompressed.png')
    print("Success")
# OUTPUT:-
# PS D:\ADS_CP> python -u "d:\ADS_CP\huffman.py"
# Huffman Compression Program
# =================================================================
# Enter 1 if you want to input an colour image file, 2 for default gray scale case:1
# Enter the filename:pic.png
# Entered string is: [[[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [150 141 142]
#   [142 136 138]
#   [137 131 133]]

#  [[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [144 138 138]
#   [138 132 134]
#   [133 127 129]]

#  [[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [140 134 136]
#   [134 128 132]
#   [128 123 127]]

#  ...

#  [[ 56  15   0]
#   [ 64  24   0]
#   [ 77  35   0]
#   ...
#   [107  68  13]
#   [103  63  11]
#   [116  76  25]]

#  [[ 54  17   0]
#   [ 59  21   0]
#   [ 62  23   0]
#   ...
#   [122  84  22]
#   [112  73  14]
#   [114  75  16]]

#  [[ 46  10   0]
#   [ 50  15   0]
#   [ 51  14   0]
#   ...
#   [119  81  16]
#   [108  70   7]
#   [102  64   1]]]
# Huffman tree with merged pathways:
# Level 0 : [[43008729, ',402[1]987635 ']]
# Level 1 : [[16849606, ',402[', '1'], [26159123, '1]987635 ', '0']]
# Level 2 : [[11386451, '1]98', '1'], [14772672, '7635 ', '0']]
# Level 3 : [[8392703, ',', '1'], [8456903, '402[', '0'], [14772672, '7635 ', '0']]
# Level 4 : [[6379969, '7635', '1'], [8392703, ' ', '0'], [8456903, '402[', '0']]
# Level 5 : [[5631176, '1', '1'], [5755275, ']98', '0'], [8392703, ' ', '0'], [8456903, '402[', '0']]
# Level 6 : [[3382461, '40', '1'], [5074442, '2[', '0'], [5755275, ']98', '0'], [8392703, ' ', '0']]
# Level 7 : [[3070677, '76', '1'], [3309292, '35', '0'], [5074442, '2[', '0'], [5755275, ']98', '0'], [8392703, ',', '1']]
# Level 8 : [[2798935, ']', '1'], [2956340, '98', '0'], [3309292, '35', '0'], [5074442, '2[', '0'], [8392703, ' ', '0']]
# Level 9 : [[2275507, '2', '1'], [2798935, '[', '0'], [2956340, '98', '0'], [3309292, '35', '0'], [5631176, '1', '1'], [8392703, ',', '1']]
# Level 10 : [[1668800, '4', '1'], [1713661, '0', '0'], [2798935, '[', '0'], [2956340, '98', '0'], [3309292, '35', '0'], [8392703, ' ', '0']]
# Level 11 : [[1644502, '3', '1'], [1664790, '5', '0'], [1713661, '0', '0'], [2798935, '[', '0'], [2956340, '98', '0'], [5631176, '1', '1'], [8392703, ',', '1']]
# Level 12 : [[1531632, '7', '1'], [1539045, '6', '0'], [1664790, '5', '0'], [1713661, '0', '0'], [2798935, '[', '0'], [2956340, '98', '0'], [8392703, ' ', '0']]
# Level 13 : [[1467425, '9', '1'], [1488915, '8', '0'], [1539045, '6', '0'], [1664790, '5', '0'], [1713661, '0', '0'], [2798935, '[', '0'], [5631176, '1', '1'], [8392703, ',', '1']]

# [['[', '1000'], ['2', '1001'], [',', '11'], [' ', '000'], ['5', '00100'], ['8', '01000'], ['9', '01001'], [']', '0101'], ['3', '00101'], ['6', '00110'], ['4', '1011'], ['0', '1010'], ['7', '00111'], ['1', '011']]
# Binary code generated:
# [ 1000
# 2 1001
# , 11
#   000
# 5 00100
# 8 01000
# 9 01001
# ] 0101
# 3 00101
# 6 00110
# 4 1011
# 0 1010
# 7 00111
# 1 011
# Your message as binary is:
# Your original file size was 301061103 bits. The compressed size is: 150561940
# This is a saving of  150499163 bits
# Compressed file generated as compressed.txt
# Decoding.......
# Your UNCOMPRESSED data is:
# [[[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [150 141 142]
#   [142 136 138]
#   [137 131 133]]

#  [[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [144 138 138]
#   [138 132 134]
#   [133 127 129]]

#  [[  2  58  95]
#   [  2  58  95]
#   [  2  58  95]
#   ...
#   [140 134 136]
#   [134 128 132]
#   [128 123 127]]

#  ...

#  [[ 56  15   0]
#   [ 64  24   0]
#   [ 77  35   0]
#   ...
#   [107  68  13]
#   [103  63  11]
#   [116  76  25]]

#  [[ 54  17   0]
#   [ 59  21   0]
#   [ 62  23   0]
#   ...
#   [122  84  22]
#   [112  73  14]
#   [114  75  16]]

#  [[ 46  10   0]
#   [ 50  15   0]
#   [ 51  14   0]
#   ...
#   [119  81  16]
#   [108  70   7]
#   [102  64   1]]]
# Observe the shapes and input and output arrays are matching or not
# Input image dimensions: (1366, 2048, 3)
# Output image dimensions: (1366, 2048, 3)
# Success