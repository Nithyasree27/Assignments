# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:11:41 2022

@author: Jothy Natarajan
"""

import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
sp=pd.read_excel("E:/imarticus/spotify.xlsx")
table=pd.crosstab(sp.A,sp.B)
stats.chi2_contingency(table)