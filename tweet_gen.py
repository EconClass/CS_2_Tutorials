import sys
import string
import random
# import collections CHEATER!

def clean_text(source_text):
    '''
    This function accesses a source file and uses punctuation_table to 
    remove punctuations and special characters.
    '''

    # Creates table of punctuations for comparison
    punctuation_table = str.maketrans( '\n-' , '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|''' )
    
    # Opens file and removes characters based on punctuation_table
    text = open(source_text)
    text_list = text.read().translate(punctuation_table).replace('--', ' ')
    text.close()
    
    # Splits text into list and lowers case of all words
    text_list = text_list.lower().split()

    # Creates NEW list of same words with out whitespace on ends
    text_list = [ word.strip() for word in text_list ]

    return text_list

def histogram(cleaned_text):
    '''
    This function takes a cleaned_text list as an argument
    and return a histogram data structure that stores each unique word along with
    the number of times the word appears in the source text.
    '''
    # Empty dictionary to be used to log occurances of words
    dictionary = dict()

    # List of unique words to be used as keys for dictionary
    unique_list = list()
    
    for word in cleaned_text:
        if word not in unique_list:
            unique_list.append(word)

    for word in unique_list:
        occurance = cleaned_text.count(word)
        dictionary[word] = occurance
    
    # *********************CHEATER!********************* #
    # Creates a dictionary of 'key: value' pairs where  
    # unique words are keys and occurances are values
    # hist_obj = collections.Counter(cleaned_text)
    # return hist_obj
    return dictionary

def unique_words(histogram_in):
    '''
    This function takes a histogram argument and 
    returns the total count of unique words in the histogram
    '''
    return len(histogram_in)

def frequency( histogram_in, word ):
    '''
    This function takes a word and histogram argument and
    returns the number of times that word appears in a text.
    '''
    if word in histogram_in:
        return histogram_in[word]
    else: return 0


def all_words(histogram_in):
    '''Calculates the total number of words in the text.'''
    total = 0
    for word in histogram_in:
        total += histogram_in[word]
    return total


def cummulative(histogram_in, num_word):
    '''
    This function sums the frequency of the words consecutively
    then appends the value to the list value of the key word.
    '''
    max_len = len(histogram_in)
    count = 0
    rand_list = []

    while( len(rand_list) <= num_word):
        rand_num = random.randint(0, max_len)
        rand_list.append(rand_num)
    
    for word in histogram_in:
        index += 1
        count += histogram_in[word][1]
        
    return

# def make_sentence(histogram_in):
#     random.randint(0, len(hist_text))
#     pass

if __name__ == "__main__":
    source = str(sys.argv[1])
    find_word = str(sys.argv[2])

    text = clean_text(source)
    hist_text = histogram(text)
    # print(random.randint(0, len(hist_text)))
    print(cummulative(hist_text, 9))
    # sum_words = all_words(hist_text)
    # print(sum_words)

    # not_same = unique_words(hist_text)
    # print('There are {} unique words in the text.'.format(not_same))

    # num_word = frequency(hist_text, find_word)
    # print('There are {} "{}"s in the text'.format(num_word, find_word))