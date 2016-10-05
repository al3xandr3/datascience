# -*- coding: utf-8 -*-

import pandas as pd

def save(df, fname="output.df"):  
    return df.to_pickle(fname)


def load(fname="output.df"):
    return pd.read_pickle(fname)

