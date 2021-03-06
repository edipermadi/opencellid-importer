# opencellid-importer

## Overview
A python script to convert OpenCellid CSV file to sqlite database

## Usage

```
$ python importer.py --db path-to-database.db --csv path-to-file.csv --mcc 525
```

## Features

- Import `.csv` or `.csv.gz` file to SQLite database (csv.gz support added by [Stig](https://github.com/stigtsp))
- Filter CSV data based on one or several [MCC](https://en.wikipedia.org/wiki/Mobile_country_code) (multiple MCC support added by [Stig](https://github.com/stigtsp))

## Documentation

- [Radio Values](doc/radio-values.md)
- [CSV File Format](doc/csv-file-format.md)
- [Database Schema](doc/database-schema.md)