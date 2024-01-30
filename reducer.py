from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None


#input from stdin
for line in sys.stdin:
    #remove leading and trailing whitespace
    line = line.strip()

    # parse input we got from maper.pu
    word,count = line.split('\t',1)
    #convert count (currenly a string ) to int
    try:
        count = int(count)
    except ValueError:
        #count was a number , so silently
        #ignore / discard this line
        continue

    if current_word == word:
        current_count += current_count
    else:
        if current_word:
            #Write Result to stout
            print("%s\t%s" % (current_word,current_count))
        current_count = count
        current_word = word



# Dont forget to output to last word the word if needed
if current_word == word:
    print("%s\t%s" % (current_word,current_count))