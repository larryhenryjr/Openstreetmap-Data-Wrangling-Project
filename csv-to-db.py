# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:58:58 2021

@author: larry
"""

import sqlite3
import csv

# Connect to the database (if it doesn't exist, it will be created in the folder that your notebook is in):
sqlite_file = 'irving_texas.db'    # name of the sqlite database file

# Connect to the database
conn = sqlite3.connect(sqlite_file)

# Get a cursor object
cur = conn.cursor()


# ============================================== #
#            Create the table nodes              #
# ============================================== #

# Drop table if exists
cur.execute("DROP TABLE IF EXISTS nodes")

# commit the changes
conn.commit()

# Create the table nodes, specifying the column names and data types:
cur.execute(''' CREATE TABLE nodes(
        id INTEGER, 
        lat INTEGER, 
        lon INTEGER, 
        user TEXT, 
        uid INTEGER, 
        version INTEGER, 
        changeset TEXT,
        timestamp TEXT)''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:
with open('nodes.csv','r', encoding="utf8") as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    # to_db = [(i['id'].decode("utf-8"), i['lat'].decode("utf-8"), i['lon'].decode("utf-8"), i['user'].decode("utf-8"),
    #         i['uid'].decode("utf-8"), i['version'].decode("utf-8"), i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) 
    to_db = [(i['id'], i['lat'], i['lon'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp']) 
               
             for i in dr]
    
print('nodes table')
    
# insert the formatted data
cur.executemany("INSERT INTO nodes(id, lat, lon, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", 
                to_db)
# commit the changes
conn.commit()


# ================================================== #
#           Create the table nodes_tags              #
# ================================================== #

# Drop table if exists
cur.execute("DROP TABLE IF EXISTS nodes_tags")

# commit the changes
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE nodes_tags(
        id INTEGER, 
        key INTEGER, 
        value TEXT, 
        type TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('nodes_tags.csv','r', encoding="utf8") as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    # to_db = [(i['id'].decode("utf-8"), i['key'].decode("utf-8"), i['value'].decode("utf-8"), i['type'].decode("utf-8")) 
    to_db = [(i['id'], i['key'], i['value'], i['type'])     
                for i in dr]
    
print('nodes_tags table')
    
# insert the formatted data
cur.executemany("INSERT INTO nodes_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()


# =========================================== #
#           Create the table ways             #
# =========================================== #

# Drop table if exists
cur.execute("DROP TABLE IF EXISTS ways")

# commit the changes
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways(
        id INTEGER, 
        user TEXT, 
        uid INTEGER, 
        version INTEGER, 
        changeset TEXT,
        timestamp TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways.csv','r', encoding="utf8") as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    # to_db = [(i['id'].decode("utf-8"), i['user'].decode("utf-8"), i['uid'].decode("utf-8"), i['version'].decode("utf-8"),
    #         i['changeset'].decode("utf-8"), i['timestamp'].decode("utf-8")) 
    to_db = [(i['id'], i['user'], i['uid'], i['version'], i['changeset'], i['timestamp'])
               for i in dr]

print('ways table')
    
# insert the formatted data
cur.executemany("INSERT INTO ways(id, user, uid, version, changeset, timestamp) VALUES (?, ?, ?, ?, ?, ?);", to_db)
# commit the changes
conn.commit()


# ================================================== #
#           Create the table ways_nodes              #
# ================================================== #

# Create the table.
#Before you (re)create the table, you will have to drop the table if it already exists: 

cur.execute('''DROP TABLE IF EXISTS ways_nodes''')
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways_nodes(
        id INTEGER, 
        node_id INTEGER, 
        position INTEGER) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways_nodes.csv','r', encoding="utf8") as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    # to_db = [(i['id'].decode("utf-8"), i['node_id'].decode("utf-8"), i['position'].decode("utf-8")) 
    to_db = [(i['id'], i['node_id'], i['position'])
               for i in dr]

print('way_nodes table')
    
# insert the formatted data
cur.executemany("INSERT INTO ways_nodes(id, node_id, position) VALUES (?, ?, ?);", to_db)
# commit the changes
conn.commit()



# ================================================== #
#            Create the table ways_tags              #
# ================================================== #

# Create the table.
#Before you (re)create the table, you will have to drop the table if it already exists: 

cur.execute('''DROP TABLE IF EXISTS ways_tags''')
conn.commit()

# Create the table, specifying the column names and data types:
cur.execute(''' CREATE TABLE ways_tags(
        id INTEGER, 
        key INTEGER, 
        value TEXT, 
        type TEXT) ''')

# commit the changes
conn.commit()

# Read in the csv file as a dictionary, format the
# data as a list of tuples:

with open('ways_tags.csv','r', encoding="utf8") as fin:
    dr = csv.DictReader(fin) # comma is default delimiter
    # to_db = [(i['id'].decode("utf-8"), i['key'].decode("utf-8"), i['value'].decode("utf-8"), i['type'].decode("utf-8")) 
    to_db = [(i['id'], i['key'], i['value'], i['type'])
               for i in dr]

print('ways_tags table')
    
# insert the formatted data
cur.executemany("INSERT INTO ways_tags(id, key, value, type) VALUES (?, ?, ?, ?);", to_db)

# commit the changes
conn.commit()


# close the connection:
conn.close()