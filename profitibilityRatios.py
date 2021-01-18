import pandas as pd
import numpy as np

ProfitibilityDataFrame = pd.DataFrame({'Year': ['2020', '2019', '2018', '2017', '2016', '2015']})


class Profitibility_Ratios():

    def gross_profit_margin(rev,revs,gp):
        i = 0
        grossMargin = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

        if(np.count_nonzero(rev) != 0):
            revenue = rev
        elif(np.count_nonzero(revs) != 0):
            revenue = revs
        else:
            revenue = [0, 0, 0, 0, 0, 0]

        while (i < len(revenue)):
            if (revenue[i] != 0 and gp[i] != 0):
                x = gp[i] / revenue[i]
                grossMargin[i] = round(x,3)
            i = i+1

        if (np.count_nonzero(grossMargin) != 0):
            ProfitibilityDataFrame['Gross Margin'] = grossMargin

    def net_margin(rev,revs,sales,ni):
        i = 0
        netMargin = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        if (np.count_nonzero(rev) != 0):
            revenue = rev
        elif (np.count_nonzero(revs) != 0):
            revenue = revs
        elif (np.count_nonzero(revs) != 0):
            revenue = sales
        else:
            revenue = [0, 0, 0, 0, 0, 0]

        while (i < len(revenue)):
            if (revenue[i] != 0 and ni[i] != 0):
                x = ni[i] / revenue[i]
                netMargin[i] = round(x,3)
            i = i+1

        if (np.count_nonzero(netMargin) != 0):
            ProfitibilityDataFrame['Net Margin'] = netMargin



    def eps_regular(eps):
        if (np.count_nonzero(eps) != 0):
            ProfitibilityDataFrame['EPS'] = eps

    def eps_diluted(eps_dil):
        if (np.count_nonzero(eps_dil) != 0):
            ProfitibilityDataFrame['EPS Diluted'] = eps_dil

    def return_on_assets(ni,ta):
        i = 0
        roa = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(ni)):
            if (ni[i] != 0 and ta[i] != 0):
                x = ni[i] / ta[i]
                roa[i] = round(x,3)
            i = i+1

        if (np.count_nonzero(roa) != 0):
            ProfitibilityDataFrame['Return On Assets'] = roa

    def return_on_equity(ni,se):
        i = 0
        roe = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        while (i < len(se)-1):
            if(ni[i] != 0 and se[i] != 0 and se[i+1] != 0):
                x = ni[i] / ((se[i] + se[i+1]) / 2)
                roe[i] = round(x, 3)
            i = i + 1
        if (np.count_nonzero(roe) != 0):
            ProfitibilityDataFrame['Return On Equities'] = roe

    def free_cash_flow(cashOp,interest,capEx):
        i = 0
        fcf = np.array([0, 0, 0, 0, 0, 0])
        while (i < len(cashOp)):
            if (cashOp[i] != 0 and interest[i] != 0 and capEx[i] != 0):
                fcf[i] = cashOp[i] + interest[i] - capEx[i]
            i = i + 1
        if (np.count_nonzero(fcf) != 0):
            ProfitibilityDataFrame['Free Cash Flow'] = fcf
