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
    
    # Splits text into list and lowers case of all items
    text_list = text_list.lower().split()

    # Creates NEW list of same items with out whitespace on ends
    text_list = [ item.strip() for item in text_list ]

    return text_list

def histogram(iterable):
    '''
    This function takes a iterable list as an argument
    and return a histogram data structure that stores each unique item along with
    the number of times the item appears in the source text.
    '''
    # Empty dictionary to be used to log occurances of items
    dictionary = dict()

    # List of unique items to be used as keys for dictionary
    unique_list = list()
    
    for item in iterable:
        if item not in unique_list:
            unique_list.append(item)

    for item in unique_list:
        occurance = iterable.count(item)
        dictionary[item] = occurance
    
    # *********************CHEATER!********************* #
    # Creates a dictionary of 'key: value' pairs where  
    # unique items are keys and occurances are values
    # hist_obj = collections.Counter(iterable)
    # return hist_obj
    return dictionary

def unique_items(histogram_in):
    '''
    This function takes a histogram argument and 
    returns the total count of unique items in the histogram
    '''
    return len(histogram_in)

def frequency( histogram_in, item ):
    '''
    This function takes a item and histogram argument and
    returns the number of times that item appears in a text.
    '''
    if item in histogram_in:
        return histogram_in[item]
    else: return 0


def all_items(histogram_in):
    '''Calculates the total number of items in the text.'''
    total = 0
    for item in histogram_in:
        total += histogram_in[item]
    return total


def cummulative_sample(histogram_in, num_iter):
    '''
    This function sums the frequency of the items consecutively
    then appends the value to the list value of the key item.
    '''
    max_len = all_items(histogram_in)
    rand_num = random.randint( 0, max_len )

    list_tuples = histogram_in.items()

    iterations = 0
    cume_sum = 0

    while (iterations < num_iter):
        for word in histogram_in:
            cume_sum += list_tuples[1]
            if cume_sum >= rand_num:
                break
        iterations += 1
    
    return 

class Dictogram(dict):
    def _dictogram(self, iterable):
        '''
        This function takes an iterable thing as an argument
        to return a histogram data structure that stores each unique item along with
        the number of times the item appears in the iterable thing.
        '''
        # Empty dictionary to be used to log occurances of items
        dictionary = dict()

        # List of unique items to be used as keys for dictionary
        unique_list = list()
        
        for item in iterable:
            if item not in unique_list:
                unique_list.append(item)

        for item in unique_list:
            occurance = iterable.count(item)
            dictionary[item] = occurance
        
        return dictionary


# class TestClass:
#     def __init__(self):
#         x = 12341234

if __name__ == "__main__":
    source = str(sys.argv[1])
    # find_item = str(sys.argv[2])
    # instancelist = [ TestClass() for i in range(7)]

    text = clean_text(source)
    # hist_text = dictogram(text)

    # print(hist_text)

    # print(histogram(instancelist))
    # print(random.randint(0, len(hist_text)))
    # print(cummulative_sample(hist_text, 9))
    # sum_items = all_items(hist_text)
    # print(sum_items)

    # not_same = unique_items(hist_text)
    # print('There are {} unique items in the text.'.format(not_same))

    # num_iter = frequency(hist_text, find_item)
    # print('There are {} "{}"s in the text'.format(num_iter, find_item))