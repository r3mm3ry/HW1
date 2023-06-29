import json
import sqlite3

with open("okved_2.json", mode='r', encoding='utf-8') as jfile:
    jlist = json.loads(jfile.read())
    con = sqlite3.connect("hw1.db")
    cur = con.cursor()
    for i in jlist:
        cur.execute("INSERT INTO okved VALUES(?, ?, ?, ?, ?)", list(i.values()))
    con.commit()
