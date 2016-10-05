# -*- coding: utf-8 -*-

import pandas as pd

def column_dtype(df, column, data_type, dformat='%Y-%m-%d'):
    
    if data_type == 'datetime':
        df[column] = pd.to_datetime(df[column], format=dformat, errors='coerce')    
    else:
        df[column] = df[column].astype(data_type)
    
    return df    


if __name__ == "__main__":
    dft = pd.DataFrame({'dt': ['2016-10-10']})
    dft.dtypes
    dft = pd.DataFrame({'dt': ['1000-01-01']})
    dft.dtypes    
    dft
    
    df2 = column_dtype(dft, 'dt', 'datetime')
    df2.dtypes
    df2
