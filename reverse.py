import sys

if __name__ == "__main__":
    # Take arguments from command line
    # Exclude the file name by slicing the list
    arguments = sys.argv[1:]

    # Trun sliced list into a string
    string = " ".join(arguments)

    # Reverse string by slicing with a negative step
    rev_string = string[::-1]

    # Print reversed string
    print(rev_string)