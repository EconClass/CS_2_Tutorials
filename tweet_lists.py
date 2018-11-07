import string

def histogram_list_of_lists(file_name):
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    words = list()
    # table = {"--": " ", "-": None}
    for line in read_words:
        mapped = line.replace("--", " ")
        split_line = mapped.rstrip().split(" ")
        for word in split_line:
            words.append(word.strip("(),!."))

    to_return = list()

    for word in words:
        wasFound=False
        for value in to_return:
            if word.lower() == value[0].lower():
                wasFound=True
                value[1] += 1
                break

        if not wasFound:
            to_add = list()
            to_add.append(word.lower())
            to_add.append(1)
            to_return.append(to_add)

    return to_return


def histogram_count_lists(file_name):
    file = open(file_name,'r')
    read_words = file.readlines()
    file.close()
    words = list()
    for line in read_words:
        split_line = line.rstrip().split(" ")
        for word in split_line:
            words.append(word.strip("(),!."))

    to_return = list()
    ones_list = list()
    ones_list.append(1)
    empty_list = list()
    ones_list.append(empty_list)
    to_return.append(ones_list)

    for word in words:
        wasFound=False
        for array in to_return:
            try:
                index = array[1].index(word.lower())
                wasFound=True
                if(array[0] == len(to_return)):
                    # print("this ran the if for " + word)
                    word_to_add = array[1].pop(index)
                    to_add = list()
                    to_add.append(array[0]+1)
                    list_list = list()
                    list_list.append(word_to_add)
                    to_add.append(list_list)
                    to_return.append(to_add)
                else:
                    # print("this ran the else for " + word)
                    word_to_add = array[1].pop(index)
                    count = array[0]
                    to_return[count][1].append(word_to_add)

                break

            except ValueError:
                pass

        if not wasFound:
            to_return[0][1].append(word.lower())

    return to_return

# text = "how How now Brown brown cow cow cow"
print(histogram_list_of_lists("the_book.txt"))
# print(histogram_count_lists("the_book.txt"))