#
# Read and write files using the built-in python file methods
#

def main():
    # open a file for writing and creating it if it doesn't exist
    myfile = open("textfile.txt", "w+")
    # open a file for appending text at the end

    # write some lines of data to the file
    for i in range(10):
        myfile.write("I am adding lines one by one\n")
    # close the file when done

    myfile.close()


# open the file back up and read the contents
# 1. open using mode 'r'
# 2 check the mode if myfile mode =="r"
# 3. read in one go or read line by line using readlines for x in f1(handle of file read)


if __name__ == "__main__":
    main()
