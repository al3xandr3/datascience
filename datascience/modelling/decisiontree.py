
from sklearn import tree
import datascience.blending.transform  as transform
import numpy  as np
import os
import subprocess


def learn (df, y):
    """
    Datascience data tree modelling
    
    Parameters
    ----------
    df : DataFrame
        Dataframe thats holds the data to build model on
    y : string 
        Label, to be used as the goal variable to learn about
        
    Example
    -------
    >>> pg = tree.learn(df, 'Churn')
    """
    Y = df[y].values
    X = transform.drop_columns(df, [y])
    X_names = list(X.columns.values)
    classifier = tree.DecisionTreeClassifier() # 
    model = classifier.fit(X.as_matrix(),Y)
    
    # 
    try:
        visualize_tree(model, X_names)
    except:
        print("Could not run dot, ie graphviz, to "
              "produce visualization. Install http://www.graphviz.org/")
    return model

def visualize_tree(model, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("dt.dot", 'w') as f:
        tree.export_graphviz(model, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        print("Could not run dot, ie graphviz, to "
             "produce visualization. Install http://www.graphviz.org/")
             

if __name__ == "__main__":
    import pandas as pd
    df = pd.DataFrame({ 'weight'  : [140, 130, 150, 170],
                         'texture' : [  1,   1,   0,   0],
                         'isOrange': [  0,   0,   1,   1]})

    learn(df, 'isOrange')

    
