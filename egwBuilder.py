import requests
import os
import sqlite3
import mysql.connector

def addEGW(username, password, bookcode, page, paragraph, text):
    
    mydb = mysql.connector.connect(
       host="bibledb.cvtfhbljhzkg.ap-southeast-2.rds.amazonaws.com",
       user=username,
       passwd=password,
       database="egw"
    )
    print(mydb) 

    mycursor = mydb.cursor()

    sql = "INSERT INTO egw_writings_complete (BOOKCODE, PAGE, PARAGRAPH, WORD) VALUES (%s, %s, %s, %s)"
    val = (bookcode, page, paragraph, text)
    mycursor.execute(sql, val)

    mydb.commit()
    reference = bookcode + " " + page + "." + paragraph
    print(mycursor.rowcount, reference, "successfully added")


username = input("username: ")
password = input("password: ")

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
   addEGW(username, password, bookcode, page, paragraph, text)




