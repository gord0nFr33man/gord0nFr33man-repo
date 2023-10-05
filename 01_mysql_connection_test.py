#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 00:43:02 2023

@author: vincentkortum
"""

#Python benötigt einen MySQL-Treiber, um Zugriff zur MySQL-Datenbank zu bekommen.
#In diesem Fall ist dies der Treiber "MySQL Connector", welcher über pip installiert wurde.
#Folgender Code stellt eine Verbindung zur Datenbank her.


import mysql.connector


my_database = mysql.connector.connect(host="localhost",user="root",password="1hkBmaD!")


print(my_database)



