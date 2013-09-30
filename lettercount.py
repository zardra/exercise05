from sys import argv

name_of_file = argv[0]

def main(filename):
    # get filename - done
    # open the file - done
    # read the file - done
    # convert to lowercase
    # convert to value
    # count how many times each letter occurs
    # print the counts in alphabetical order
    #filename = raw_input("Enter filename: ")

    f = open(filename)
    filetext = f.read()
    f.close()

    char_list = [0] * 26
    

    for char in filetext:
        #convert to lowercase
        #convert to ASCII value
        #convert to 0 - 25
        #put in list

        char_ord = ord(char.lower())-97
        if char_ord >= 0 and char_ord <=25:
   
            char_list[char_ord] += 1
    return char_list

main(name_of_file)