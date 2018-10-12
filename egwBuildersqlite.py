import requests
import os
import sqlite3
import mysql.connector

def addEGW(bookcode, page, paragraph, text):
        conn = sqlite3.connect('egw_writings_complete.db')
        conn.execute("INSERT INTO egw_writings_complete (BOOKCODE, PAGE, PARAGRAPH, WORD) VALUES(?, ?, ?, ?)", (bookcode, page, paragraph, text));
        conn.commit()
        reference = bookcode + " " + page + "." + paragraph
        print(reference, " successfully added")
        conn.close()    


file = open("egw-comp.TXT", "r")
lines = file.read()
split = lines.split("}")
del split[len(split)-1]

for line in split:
  if line!="":
   reference = line.split("{")
   text = reference[0]
   getbookcode = reference[1].split(" ")
   bookcode = getbookcode[0]
   getpage = getbookcode[1].split(".")
   page = getpage[0]
   paragraph = getpage[1] 
   addEGW(bookcode, page, paragraph, text)




