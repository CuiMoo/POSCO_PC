import sqlite3

conn = sqlite3.connect('recorddb.sqlite3')
c = conn.cursor()

#create table for data storage
c.execute("""CREATE TABLE IF NOT EXISTS VC-record(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    RCid TEXT,
    motor TEXT,
    tempDE REAL,
    tempNDE REAL,
    vib-V REAL,
    vib-H REAL,
    vib-A REAL,
    oil REAL,
    date TEXT""")

def insertRecord():
    with conn:
        command = 'INSERT INTO VC-record VALUES(?,?,?,?,?,?,?,?,?,?)'