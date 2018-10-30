import random  
import sys

def word_list (file):
    words = open(file)
    words_list = words.read().split('\n')
    words.close()
    return words_list

if __name__ == '__main__':
    sample_size = int(sys.argv[1])
    words_list = word_list('/usr/share/dict/words')
    rand_sample = random.sample( words_list, sample_size )
    print(" ".join(rand_sample))




