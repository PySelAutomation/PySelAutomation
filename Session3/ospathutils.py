import os
from os import path
import datetime
from datetime import datetime, date, timedelta
import time


def main():
    print(os.name)
    # check for item existence and type
    print("Item exist:", path.exists("textfile.txt"))
    # item is file
    print("Item is a file :", path.isfile("textfile.txt"))
    # item is directory

    # work with file path
    print("File path is :", path.realpath("textfile.txt"))
    print("File path and name is :", path.split(path.realpath("textfile.txt")))

  # Get the modification time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.fromtimestamp(path.getmtime("textfile.txt")))


      # claculate how long ago the item was modified

    # now - modified time
if __name__ == "__main__":
    main()
