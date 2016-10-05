# -*- coding: utf-8 -*-
"""
Created on 4 October 2016

@author: A3xandr3
"""

import psycopg2
import pandas as pd
import os;
   
class Postgres(object):

    def __init__(self, connection_params=None):
        """
        Postgres database access
        
        Parameters
        ----------
        connection_params : dictionary
            Connection parameters, see example
            
        Example
        -------
        """             
        self.conn = None
        self.cursor = None

        if connection_params:
            self.open(connection_params)


    def open(self,connection_params):
        """
        Opens a new database connection.
        """        
        self.connection_params = connection_params
    

        self.conn = psycopg2.connect(database = self.connection_params['database'],
                                     
        user = self.connection_params['user'],
        password = self.connection_params['password'],
        host = self.connection_params['host'],
        port = self.connection_params['port'])
            
        self.cursor = self.conn.cursor()



    def close(self):
        """
        Function to close a database connection.
        """
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()



    def query(self,sql):
        """
        Function to query any other SQL statement.
        This function is there in case you want to execute any other sql
        statement other than a write or get.
        
        Parameters
        ----------
        sql : string
            SQL Query string
        
        Returns
        -------
        db.cursor
        
        Examples
        --------
        >>> q = pg.query("select * from <table> limit 10;")
            for row in q.fetchall():
                print(row)
        """
        self.cursor.execute(sql)
        return self.cursor


    def toCSV(self, sql, fname="output.csv"):
        """
        Utility function that converts a dataset into CSV format
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        colnames = [desc[0] for desc in self.cursor.description]
        with open(fname,'a') as file:
            file.write(",".join([str(j) for i in colnames for j in i]))
            file.write(",".join([str(j) for i in data for j in i]))      
            
    
    def toDataFrame(self, sql):
        """
        Utility function that converts a dataset into pandas dataframe        
        """
        self.cursor.execute(sql)
        colnames = [desc[0] for desc in self.cursor.description]
        return pd.DataFrame(self.cursor.fetchall(), columns=colnames)



if __name__ == "__main__":
     
     # query     
     q = pg.query("select * from <table> limit 10;")
     for row in q.fetchall():
            print(row)

     # to DataFrame            
     q2 = pg.toDataFrame("select * <table> limit 10;")            
     print q2


