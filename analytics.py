
import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant

def compute_analytics(df):
    price = df['price']
    mean = price.mean()
    std = price.std()
    z = (price.iloc[-1] - mean) / std if std > 0 else 0
    return mean, std, z

def hedge_ratio(x, y):
    x = add_constant(x)
    model = OLS(y, x).fit()
    return model.params[1]
