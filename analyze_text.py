import sys
import string
import collections

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
    # Creates a dictionary of 'key: value' pairs where  
    # unique words are keys and occurances are values
    hist_obj = collections.Counter(cleaned_text)
    return hist_obj

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
   


if __name__ == "__main__":
    source = str(sys.argv[1])
    find_word = str(sys.argv[2])

    text = clean_text(source)
    hist_text = histogram(text)
    
    not_same = unique_words(hist_text)
    print('There are {} unique words in the text.'.format(not_same))

    num_word = frequency(hist_text, find_word)
    print('There are {} "{}" in the text'.format(num_word, find_word))