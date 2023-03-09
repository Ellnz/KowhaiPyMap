# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:11:09 2023

@author: EllisNimick
"""

import sqlite3

# tuple for SQLite
book_list = [
    (1962, "Silent Spring", "Rachel Carson"),
    (2020, "The Book of Trespass", "Nick Hayes"),
    (1990, "Last Chance to See", "Douglas Adams"),
    (1994, "The Future Eaters", "Tim Flannery"),
    (2019, "The Uninhabitable Earth", "David Wallace-Wells"),
    (2016, "Dark Money", "Jane Mayer")
]

# create empty database
connection = sqlite3.connect("books.db")
# communicate with database
cursor = connection.cursor()

# create table within database and 
cursor.execute("create table books (published_year integer, book_title text, author_name text)")
cursor.executemany("insert into books values (?,?,?)", book_list)
# save changes immediately
connection.commit()

# print database rows
for row in cursor.execute("select * from books"):
    print(row)

# print specified row
cursor.execute("select * from books where author_name=:a", {"a": "Douglas Adams"})
book_search = cursor.fetchall()
print(book_search)


# Terminate connection
connection.close()
