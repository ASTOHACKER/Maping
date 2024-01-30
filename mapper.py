#Linux Sys
# import sys 
# for line in sys.stdin:
#     #remove leading and trailing whitespace ลบช่องว่างนำหน้าและต่อท้าย
#     line = line.strip() #ลบช่องว่างนำหน้าและต่อท้าย
#     # Split The Line into Words
#     words = line.split()
#     #Increase Counters
#     for word in words:
#         print('%s\t%s' % (word,1))

# Python Test By self

import sys
from os.path import exists
FILE_PATH = ("E:\Dataset\Maping\File.txt")
FILE_SET = ("E:\Dataset\Maping\success.txt")
if not exists:
    {}
else :
    f = open(FILE_PATH, "r", encoding="utf-8")
    word = f.read()


for line in sys.stdin:
    line = word.strip()
    words = line.split(' ')
    for word in words:
        print('%s\t%s' % (word,1))
        if word == None or word == False:
            print("Error")
            continue

