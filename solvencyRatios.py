import pandas as pd
import numpy as np
SolvencyDataFrame = pd.DataFrame({'Year': ['2020', '2019', '2018', '2017', '2016', '2015']})

class Solvency_Ratios():
    def asset_equity_ratio(totAssets,totEquity):
        i = 0
        tdr = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(totAssets)):
            if (totAssets[i] != 0 and totEquity[i] != 0):
                x = (totAssets[i] - totEquity[i])/totAssets[i]
                tdr[i] = round(x,3)
            i = i+1

        if (np.count_nonzero(tdr) != 0):
            SolvencyDataFrame['Asset Equity Ratio'] = tdr

    def debt_equity_ratio(totL,totEq):
        i = 0
        #total debt/ total equity
        der = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(totL)):
            if (totL[i] != 0 and totEq[i] != 0):
                x = totL[i] / totEq[i]
                der[i] = round(x,3)
            i = i+1
        if(np.count_nonzero(der) != 0):
            SolvencyDataFrame['Debt Equity Ratio'] = der

    def equity_multiplier(a,e):
        i = 0
        #assets/equity
        em = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(a)):
            if (a[i] != 0 and e[i] != 0):
                x = a[i] / e[i]
                em[i] = round(x,3)
            i = i+1
        if (np.count_nonzero(em) != 0):
            SolvencyDataFrame['Equity Multiplier'] = em