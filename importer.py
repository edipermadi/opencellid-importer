#!/usr/bin/env python

def main():
    import sys
    import csv

    with open(sys.argv[1]) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print ', '.join(row)
            break

    pass

if __name__ == '__main__':
    main()