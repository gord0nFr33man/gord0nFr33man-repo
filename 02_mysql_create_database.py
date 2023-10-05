#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:43:57 2023

@author: vincentkortum
"""
#Erstellen einer Datenbank namens mydatabase mittels MySQL-statement CREATE DATABASE.
#Der name.cursor() Befehl ist dazu da, um MySQL-statements ausführen zu können und um mit der MySQL-Datenbank kommunizieren zu können.


import mysql.connector


my_database = mysql.connector.connect(host="localhost",user="root",password="1hkBmaD!")


my_cursor = my_database.cursor()

my_cursor.execute("CREATE DATABASE mydatabase")



