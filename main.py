import sys
 from total import total
from interactive import interactive
n = sys.argv[1]

with open('data.csv','r') as file:
    next_line = file.readline()

    while next_line:
        next_line = file.readline()
        print(next_line)
        import sys
""" n = sys.argv[1]

with open('data.csv','r') as file:
    next_line = file.readline()

    while next_line:
        next_line = file.readline()
        print(next_line) """
FILENAME = 'data.tsv'
YEAR = 1992
#total(FILENAME,YEAR)
interactive(FILENAME)