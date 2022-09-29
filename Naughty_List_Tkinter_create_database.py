# This program will create a database class

from tkinter import *

from PIL import ImageTk,Image

#sqlite is built-in Python
import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
                '''CREATE TABLE IF NOT EXISTS NAUGHTY_LIST( 
                id INTEGER PRIMARY KEY,
                childID integer,
                fName text,
                lName text,
                city text,
                state text,
                mobileNo text,
                behavior text)''')
        print('Table created sucessfully')
        self.conn.commit()
      
    def fetch(self):
        self.cur.execute("SELECT * FROM NAUGHTY_LIST")
        rows = self.cur.fetchall()
        return rows

    def searchID(self,childID):
        self.cur.execute("SELECT * FROM NAUGHTY_LIST WHERE childID =?",(childID,))
        result = self.cur.fetchall()
        return result

    def insert(self, childID, fName, lName, city, state, mobileNo, behavior):
        try:
            self.cur.execute("INSERT INTO NAUGHTY_LIST VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                            (childID, fName, lName, city, state, mobileNo, behavior))
            self.conn.commit()
            print('Record Added Successfully')
        except:
            print("Error in operation-DB.insert")
            conn.rollback()

    def remove(self,childID):
        try:
            self.cur.execute("DELETE FROM NAUGHTY_LIST WHERE childID=?", (childID,))
            self.conn.commit()
            print("Sucessfully Deleted")
        except:
            print('Error in operation-DB.remove')
            conn.rollback()

    def update(self, childID, fName, lname, city, state, mobileNo, behavior):
        try:
            self.cur.execute('''UPDATE NAUGHTY_LIST SET
                         fName = ?,
                         lName = ?,
                         city = ?,
                         state = ?,
                         mobileNo = ?,
                         behavior = ?
                         WHERE childID = ?''',
                        (fName,lname, city, state, mobileNo, behavior, childID))
            print("Sucessfully Updated")
            self.conn.commit()
        except:
            print('Error in operation-DB.update')
            conn.rollback()

    def __del__(self):
        self.conn.close()
