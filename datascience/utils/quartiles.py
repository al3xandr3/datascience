# -*- coding: utf-8 -*-

# 
def boxplot_values (data_df):
    x =  data_df
    return [
         x.min().values[0]
         ,x.quantile(.25).values[0]
        ,x.median().values[0]
        ,x.quantile(.75).values[0]
        ,x.max().values[0]
        ]

#print boxplot_values([377,571,248,573,341,314,1007,398,158,192,405,404,286,176,167,900])
