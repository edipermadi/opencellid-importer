import sqlite3

CREATE_TABLE_SQL = '''
CREATE TABLE IF NOT EXISTS cells (
    id integer PRIMARY KEY AUTOINCREMENT,
    radio VARCHAR(16) NOT NULL,
    mcc INTEGER NOT NULL,
    net INTEGER NOT NULL,
    area INTEGER NOT NULL,
    cell INTEGER NOT NULL,
    unit INTEGER NOT NULL,
    lon REAL NOT NULL,
    lat REAL NOT NULL,
    range INTEGER NOT NULL,
    samples INTEGER NOT NULL,
    changeable INTEGER NOT NULL,
    created INTEGER NOT NULL,
    updated INTEGER NOT NULL,
    average_signal INTEGER NOT NULL
);'''

CREATE_INDEX_SQLS = (
    'CREATE INDEX cell_radio ON cells (radio);',
    'CREATE INDEX cell_mcc_net ON cells (mcc, net);',
    'CREATE INDEX cell_radio_mcc_net ON cells (radio, mcc, net);',
    'CREATE INDEX cell_area_cell ON cells (area, cell);',
    'CREATE INDEX cell_radio_area_cell ON cells (radio, area, cell);',
    'CREATE INDEX cell_mcc_net_area_cell ON cells (mcc, net, area, cell);',
    'CREATE INDEX cell_radio_mcc_net_area_cell ON cells (radio, mcc, net, area, cell);'
)


INSERT_ENTRY_SQL = '''
INSERT INTO cells (
    radio, mcc, net, area, cell, unit, lon, lat, range, samples, changeable, created, updated, average_signal
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

class CellIdDatabase(object):
    def __init__(self, filename):
        self.conn = sqlite3.connect(filename)
        self.counter = 0

    def __del__(self):
        self.conn.close()

    def create_tables(self):
        self.conn.execute(CREATE_TABLE_SQL)
        for sql in CREATE_INDEX_SQLS:
            self.conn.execute(sql)
        self.conn.commit()

    def insert(self, values):
        self.counter += 1

        print "insert #{}".format(self.counter)
        self.conn.executemany(INSERT_ENTRY_SQL, values)
        self.conn.commit()