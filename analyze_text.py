import sys


def clean_text(source_text):
    '''
    Removes empty spaces, punctuations and ...
    '''
    manifesto = open('the_book.txt')
    manifesto_list = manifesto.read().replace('\n', ' ')
    manifesto.close()
    manifesto_list = manifesto_list.split()
    manifesto_list = [ word.strip() for word in manifesto_list ]
    print(manifesto_list)

def histogram(cleaned_text):
    '''
    This function takes a source_text as an argument
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

    clean_text('the_book.txt')