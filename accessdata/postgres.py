# -*- coding: utf-8 -*-
"""
Created on 4 October 2016

@author: A3xandr3
"""

import psycopg2
import pandas as pd
import os;
   
class Postgres(object):
 


    #######################################################################
    #
    ## The constructor of the Database class
    #
    #  The constructor can either be passed the name of the database to open
    #  or not, it is optional. The database can also be opened manually with
    #  the open() method or as a context manager.
    #  on Windows Install lib: http://stickpeople.com/projects/python/win-psycopg/
    #
    #  @param url Optionally, the url of the database to open.
    #
    #  @see open()
    #
    #######################################################################

    def __init__(self, url=None):
        self.conn = None
        self.cursor = None

        if url:
            self.open(url)



    #######################################################################
    #
    ## Opens a new database connection.
    #
    #  This function manually opens a new database connection. The database
    #  can also be opened in the constructor or as a context manager.
    #
    #  @param url The url of the database to open.
    #
    #  @see \__init\__()
    #
    #######################################################################

    def open(self,url):
        self.url = url
    
        # Access credentials via the passed on url. The url must
        # be parsed with the urlparse library. 
        self.conn = psycopg2.connect(database = self.url['database'],
                                     
        user = self.url['user'],
        password = self.url['password'],
        host = self.url['host'],
        port = self.url['port'])
            
        self.cursor = self.conn.cursor()



    #######################################################################
    #
    ## Function to close a datbase connection.
    #
    #  The database connection needs to be closed before you exit a program,
    #  otherwise changes might be lost. You can also manage the database
    #  connection as a context manager, then the closing is done for you. If
    #  you opened the database connection with the open() method or with the
    #  constructor ( \__init\__() ), you must close the connection with this
    #  method.
    #
    #  @see open()
    #
    #  @see \__init\__()
    #
    #######################################################################
    
    def close(self):
        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()



    #######################################################################
    #
    ## Function to query any other SQL statement.
    #
    #  This function is there in case you want to execute any other sql
    #  statement other than a write or get.
    #
    #  @param sql A valid SQL statement in string format.
    #
    #######################################################################

    def query(self,sql):
        self.cursor.execute(sql)
        return self.cursor


    #######################################################################
    #
    ## Utility function that converts a dataset into CSV format.
    #
    #  @param sql, the string with the sql needed
    #
    #  @param fname The file name to store the data in.
    #
    #  @see get()
    #
    #######################################################################
    
    def toCSV(self, sql, fname="output.csv"):
        query = self.cursor.execute(sql)
        data = query.fetchall()
        with open(fname,'a') as file:
            file.write(",".join([str(j) for i in data for j in i]))      
            
    #######################################################################
    #
    ## Utility function that converts a dataset into pandas dataframe
    #
    #  @param sql, the string with the sql needed
    #
    #  @param fname The file name to store the data in.
    #
    #  @see get()
    #
    #######################################################################
    
    def toDataFrame(self, sql):
        self.cursor.execute(sql)
        return pd.DataFrame(self.cursor.fetchall())



if __name__ == "__main__":
     pg = Postgres({'host': '<11.111.11.1>', 'database': '<db>', 'port': 5432, 'user': '<user>', 'password': os.environ['PGPASSWORD']})
     
     # query     
     q = pg.query("select * from <table> limit 10;")
     for row in q.fetchall():
            print(row)

     # to DataFrame            
     q2 = pg.toDataFrame("select * <table> limit 10;")            
     print q2


