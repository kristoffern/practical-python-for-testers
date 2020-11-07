from datetime import datetime
from termcolor import colored


def printMatchingLine(filehandle, keyword, color):        
    line = filehandle.readline()    
    if line != '' and keyword in line:
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        line_without_color = '[{}]: {}'.format(timestamp, line.strip())
        print(colored(line_without_color, color))

if __name__ == '__main__':
    firstFile = open('/opt/PFT/DataDigger/first.log', 'r')
    secondFile = open('/opt/PFT/DataDigger/second.log', 'r')

    while True:
        printMatchingLine(firstFile, 'Allocated', 'blue')
        printMatchingLine(secondFile, 'Refilling', 'green')