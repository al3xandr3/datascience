
# User Churn Modeling and Predicting
# http://blog.yhat.com/posts/predicting-customer-churn-with-sklearn.html

import pandas as pd
import datascience.accessdata.database as db
import datascience.accessdata.file     as fl
import datascience.blending.transform  as transform
import datascience.modelling.decisiontree as treemodel
import os


####################################################
# Get get a sample of data from database
####################################################
 
import pickle; connection_params = pickle.load( open( "db.p", "rb" ) )
pg = db.Postgres({'host':      connection_params['host']
                  ,'database': connection_params['database']
                  ,'port':     connection_params['port']
                  ,'user':     connection_params['user']
                  ,'password': connection_params['password']})

# export to csv
pg.toCSV("select * from groups order by random() limit 10000;", "churn.csv")


df = pg.toDataFrame("select * from groups order by random() limit 10000;")
pg.close()



####################################################
# transforming columns to correct data types
####################################################

df = transform.column_dtype(df, 'key_user',            'string')
df = transform.column_dtype(df, 'login_first_dt',      'datetime')
df = transform.column_dtype(df, 'cnt_call_mins',       'float')
df = transform.column_dtype(df, 'cnt_group_call_mins', 'float')
df.dtypes

# save into a native format, that preserves data types
fl.save(df, "churn.df")



####################################################
# Specify Churn label, prepare data for model
####################################################
df = fl.load("churn.df")
df = transform.make_binary(df, 'month2_type')
df['churn'] = df['inactive']

# drop uneeded cols
drop = ['habitual', 'inactive', 'infrequent', 'key_user', 'month2_type', 
        'country',  'login_first_dt', 'surv_flag_next_month_active',
        'surv_next_month_days_active']
df2 = transform.drop_columns(df, drop)



####################################################
# Sample / split data
####################################################


####################################################
# Modeling optimization iteration:
#  build model
#  apply
#  measure performance
####################################################

model = treemodel.learn(df2, 'churn')



####################################################
# Apply Model (optimized model)
####################################################



####################################################
# Measure performance
####################################################


