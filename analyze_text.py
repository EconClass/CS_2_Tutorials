import sys
import string

def clean_text(source_text):
    '''
    Removes empty spaces, punctuations and special characters
    '''
    punctuation_table = str.maketrans( '\n-' , '  ', '''1234567890~!@#$.,%^&*()_+?/`[];'":|''' )

    text = open('the_book.txt')
    text_list = text.read().translate(punctuation_table).replace('--', ' ')
    text.close()
    
    text_list = text_list.lower().split()
    text_list = [ word.strip() for word in text_list ]
    return text_list

def histogram(cleaned_text):
    '''
    This function takes a cleaned_text list as an argument
    and return a histogram data structure that stores each unique word along with
    the number of times the word appears in the source text.
    '''
    pass

def unique_words(histogram_in):
    '''
    This function takes a histogram argument and 
    returns the total count of unique words in the histogram
    '''
    pass

def frequency(word, histogram_in):
    '''
    This function takes a word and histogram argument and
    returns the number of times that word appears in a text.
    '''
    pass


if __name__ == "__main__":

    text = clean_text('the_book.txt')
    print(text)
    # hist_text = histogram(text)