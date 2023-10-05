#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 17:37:39 2023

@author: vincentkortum
"""

import mysql.connector


my_database = mysql.connector.connect(host="localhost",user="root",password="1hkBmaD!",database="mydatabase")

my_cursor = my_database.cursor()


#Auflisten aller erstellten Tabellen
my_cursor.execute("SHOW TABLES")

for x in my_cursor:
  print(x)



#Tabelle verwerfen
#drop_table = my_cursor.execute("DROP TABLE tabellenname")
#my_cursor.execute(drop_table) 
  

#Tabelle für Temperaturwerte des Chips anlegen
#my_cursor.execute("CREATE TABLE temperaturwerte (temp_wert_chip VARCHAR(255))")


#Tabelle für Beschleunigungswerte anlegen
#my_cursor.execute("CREATE TABLE beschleunigungsswerte (acc_wert_x VARCHAR(255), acc_wert_y VARCHAR(255), acc_wert_z VARCHAR(255))") 


#Tabelle für Gyrometerwerte anlegen
my_cursor.execute("CREATE TABLE gyrometerwerte (gyro_wert_x VARCHAR(255), gyro_wert_y VARCHAR(255), gyro_wert_z VARCHAR(255))") 


#Tabelle für Magnetometerwerte anlegen
#my_cursor.execute("CREATE TABLE magnetometerwerte (magnet_wert_x VARCHAR(255), magnet_wert_y VARCHAR(255), magnet_wert_z VARCHAR(255))")





my_cursor.close()
my_database.close()



