# import datetime here
from bc import bc


# define a method here called printMatchingLine(filehandle, keyword, color):
	#read the next line from filehandle and assign to variable line
    # check if line is not empty & contains keyword
        # create a timestamp (datetime.now() and strftime()) to use on printout
        # print the line found with color coding - [TIMESTAMP]: LINE

if __name__ == '__main__':
    # Open a file handle for the first file: /opt/PFT/DataDigger/first.log
    # Open a file handle for the first file: /opt/PFT/DataDigger/second.log
    secondFile = open('/opt/PFT/DataDigger/second.log', 'r')

    while True:
        # call printMatchingLine() for the next line in the first file
        # call printMatchingLine() for the next line in the second file