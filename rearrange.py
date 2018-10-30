import random
import sys

'''
Take arguments form command line with argv from sys module
Slice list of arguments by slicing excluding the file name
'''
pick_words = sys.argv[1:]

if __name__ == "__main__":
    '''
    Take a random sample of elements from pick_words list
    Sample size encompasses entire list
    ''' 
    gen_list = random.sample( pick_words, len(pick_words) )

    "Turn sample into a string then print it"
    gen_str = ' '.join(gen_list)
    print(gen_str)
