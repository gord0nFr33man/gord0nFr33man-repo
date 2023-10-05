# gord0nFr33man-repo
Working on a MySQL-database (8.0.20) using Python 3.9.7 in Spyder IDE 5.1.5 that at some point 
will be able to store measuring data provided by a MPU9255 sensor chip unit mounted on a RC-Car.


Future plans:
- feeding the tables with a predefined static set of data, using MySQL-statements in Spyder IDE.
- showing the raw content of the tables in Spyder's console
- adding a time stamp to the predefined set of data that will be injected into the tables
- feeding the tables with pseudorandomly generated data, using import random.
- feeding the tables with these pseudorandomly generated data within a update frequency of 100ms.

*The ETA on these future plans is somewhere between a very few days and the end of time.

Changelog:
10/05/2023
The program 04_mysql_create_tables.py has been created. It has created a few new tables in my database.
I'm not sure about the general idea behind the layout/format of these tables though.
Adjustments will have to be made either way.

10/04/2023
The program 03_mysql_show_databases.py has been created. It serves the purpose to verify the existence of all databases running on my system.

10/02/2023
The program 02_mysql_create_database.py has been created. It serves the purpose to create a new database named 'mydatabase'.
The program 01_mysql_connection_test.py has been created. It serves the purpose to build a connection to the 'mysql'-database.
Installation procress of MySQLWorkbench8.0.20 has finished. The workbench seems to work and is running in the background.
Installation process of mysql-8.0.20-macos10.15-x86_64 has finished. The MySQL-server is up and running under version 8.0.20.
