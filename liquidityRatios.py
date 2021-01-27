import pandas as pd
import numpy as np
LiquidityDataFrame = pd.DataFrame({'Year': ['2020', '2019', '2018', '2017', '2016', '2015']})


class Liquidity_Ratios():

    def current_ratio(curAssets, curLiabilities):
        curRatio = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        i = 0
        while (i < len(curAssets)):
            if (curAssets[i] != 0 and curLiabilities[i] != 0):
                x = curAssets[i] / curLiabilities[i]
                curRatio[i] = round(x,3)
            i = i+1
        if (np.count_nonzero(curRatio) != 0):
            LiquidityDataFrame['Current Ratio'] = curRatio

    def working_capital(currentAssets,currentLiabilities):
        i = 0
        workingCapital = np.array([0, 0, 0, 0, 0, 0])
        while (i < len(currentAssets)):
            if (currentAssets[i] != 0 and currentLiabilities[i] != 0):
                x = currentAssets[i] - currentLiabilities[i]
                workingCapital[i] = round(x, 3)
            i = i + 1
        if (np.count_nonzero(workingCapital) != 0):
            LiquidityDataFrame['Working Capital'] = workingCapital

    def cash_ratio(cash, currentLiabilities):
        i = 0
        cashRatio = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(cash)):
            if (cash[i] != 0 and currentLiabilities[i] != 0):
                x = cash[i] / currentLiabilities[i]
                cashRatio[i] = round(x, 3)
            i = i + 1
        if (np.count_nonzero(cashRatio) != 0):
            LiquidityDataFrame['Cash Ratio'] = cashRatio

    def quick_ratio(ca, inv, ppe, cl):
        i = 0
        quickRatio = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(ca)):
            if (ca[i] != 0 and inv[i] != 0 and ppe[i] != 0 and cl[i] != 0):
                x = (ca[i] - inv[i] - ppe[i])/cl[i]
                quickRatio[i] = round(x, 3)
            i = i + 1
        if (np.count_nonzero(quickRatio) != 0):
            LiquidityDataFrame['Quick Ratio'] = quickRatio

    def cash_debt_coverage(netCash, curL):
        i = 0
        cdc = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(curL)-1):
            if(netCash[i] != 0 and curL[i] != 0 and curL[i+1] != 0):
                x = netCash[i] / ((curL[i] + curL[i+1]) / 2)
                cdc[i] = round(x, 3)
            i = i + 1
        if (np.count_nonzero(cdc) != 0):
            LiquidityDataFrame['Cur Cash/Debt Coverage'] = cdc