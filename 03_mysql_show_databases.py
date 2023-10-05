#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 19:10:03 2023

@author: vincentkortum
"""

import mysql.connector


my_database = mysql.connector.connect(host="localhost",user="root",password="1hkBmaD!",database="mydatabase")


my_cursor = my_database.cursor()


#Auflisten aller vorhandenen Datenbanken
my_cursor.execute("SHOW DATABASES")
for x in my_cursor:
    print(x)