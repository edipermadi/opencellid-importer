#!/usr/bin/env python

COLUMNS = ['radio', 'mcc', 'net', 'area', 'cell', 'unit', 'lon', 'lat', 'range', 'samples', 'changeable', 'created',
           'updated', 'averageSignal']


def do_import(db_filename, csv_filename, mcc = None):
    import csv
    from opencellid.db import CellIdDatabase

    database = CellIdDatabase(db_filename)
    database.create_tables()

    entries = []
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row == COLUMNS:
                continue
            elif mcc and int(mcc) != int(row[1]):
                continue

            entries.append(row)
            if len(entries) == 65536:
                database.insert(entries)
                entries = []

        if entries:
            database.insert(entries)


def main():
    import argparse

    parser = argparse.ArgumentParser('importer.py')
    parser.add_argument('--db', dest='db', action='store', required=True, type=str,
                        help='path to SQLite3 output database filename')
    parser.add_argument('--csv', dest='csv', action='store', required=True, type=str,
                        help='path to open-cell-id CSV source file')
    parser.add_argument('--mcc', dest='mcc', action='store', required=False, type=int,
                        help='optional MCC code to filter entries')
    args = parser.parse_args();
    do_import(args.db, args.csv, args.mcc)


if __name__ == '__main__':
    main()
