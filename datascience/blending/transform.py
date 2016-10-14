# -*- coding: utf-8 -*-

import pandas as pd


def column_dtype(df, column, data_type, dformat='%Y-%m-%d'):
    """
    Datascience data transform
    
    Parameters
    ----------
    df : DataFrame
        Dataframe 
    column : string 
        Column to apply a data type change
    data_type : string 
        Data Type to apply to the column
    data_type : string 
        Optional data type to be used in some cases
        
    Example
    -------
    >>> df = transform.column_dtype(df, 'key_user','string')
    """
    if data_type == 'datetime':
        df[column] = pd.to_datetime(df[column], format=dformat, errors='coerce')    
    else:
        df[column] = df[column].astype(data_type)
    
    return df    




def make_binary(df, column, _axis=1):
    """
    One Hot encoding tranformation
    
    Parameters
    ----------
    df : DataFrame
        Dataframe 
    column : string 
        Column to apply a data type change
    data_type : string 
        Data Type to apply to the column
    data_type : string 
        Optional data type to be used in some cases
        
    Example
    -------
    >>> df = transform.column_dtype(df, 'key_user','string')
    """
    dum = df[column]
    dum_extracted = pd.get_dummies(dum)
    return  pd.concat([df,dum_extracted], axis=_axis, join='outer')




def drop_columns(df, columns_arr):
    """
       Datascience data transformation
        
        Parameters
        ----------
        df : DataFrame
            Dataframe to apply transformation to
        columns_arr : Array
            Array of string of the lists to drop
            
        Example
        -------
        >>> pg = transform.drop_columns(df, ['State','Area Code','Phone','Churn?'])
        """                    
    return df.drop(columns_arr, axis=1)     




def select_columns(df, columns_arr):
    """
       Datascience data transformation
        
        Parameters
        ----------
        df : DataFrame
            Dataframe to apply transformation to
        columns_arr : Array
            Array of string of the lists to select
            
        Example
        -------
        >>> pg = transform.drop_columns(df, ['State','Area Code','Phone','Churn?'])
        """                    
    return df[columns_arr] 





def normalize(df, column):
    # TODO
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X = scaler.fit_transform(X)




if __name__ == "__main__":
    dft = pd.DataFrame({'dt': ['2016-10-10']})
    dft.dtypes
    dft = pd.DataFrame({'dt': ['1000-01-01']})
    dft.dtypes    
    dft
    
    df2 = column_dtype(dft, 'dt', 'datetime')
    df2.dtypes
    df2
