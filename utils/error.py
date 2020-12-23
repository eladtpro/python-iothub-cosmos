#import sys
from traceback import print_exc

def printError():
    print_exc()
    #type, value, traceback = sys.exc_info()
    #print(f"Error {value} %s" % (value.filename, value.strerror))
