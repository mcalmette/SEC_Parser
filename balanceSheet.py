from bs4 import BeautifulSoup
import pandas as pd
import re
from tqdm import tqdm
import numpy as np
from liquidityRatios import Liquidity_Ratios
from liquidityRatios import LiquidityDataFrame
from profitibilityRatios import Profitibility_Ratios
from profitibilityRatios import ProfitibilityDataFrame


BalanceSheetDataFrame = pd.DataFrame({'Year': [2020, 2019, 2018, 2017, 2016, 2015]})
cash = np.array([0, 0, 0, 0, 0, 0])
currentAssets = np.array([0, 0, 0, 0, 0, 0])
currentLiabilities = np.array([0, 0, 0, 0, 0, 0])
assets = np.array([0, 0, 0, 0, 0, 0])
lase = np.array([0, 0, 0, 0, 0, 0])
stockholdersequity = np.array([0, 0, 0, 0, 0, 0])
accountsReceivable = np.array([0, 0, 0, 0, 0, 0])
accountsPayable = np.array([0, 0, 0, 0, 0, 0])
netInventory = np.array([0, 0, 0, 0, 0, 0])
plantPropertyEq = np.array([0, 0, 0, 0, 0, 0])
accruedLiabilities = np.array([0, 0, 0, 0, 0, 0])
retainedEarnings = np.array([0, 0, 0, 0, 0, 0])
longTermDebt = np.array([0, 0, 0, 0, 0, 0])
prepaidExpenses = np.array([0, 0, 0, 0, 0, 0])
#flags for if context ref is triggered

IncomeStatementDataFrame = pd.DataFrame({'Year': [2020, 2019, 2018, 2017, 2016, 2015]})
netRevenue = np.array([0, 0, 0, 0, 0, 0])
grossProfit = np.array([0, 0, 0, 0, 0, 0])
revenues = np.array([0, 0, 0, 0, 0, 0])
salesRevenue = np.array([0, 0, 0, 0, 0, 0])
costOfGoodsServicesSold = np.array([0, 0, 0, 0, 0, 0])
costOfRevenue = np.array([0, 0, 0, 0, 0, 0])
costsAndExpense = np.array([0, 0, 0, 0, 0, 0])
operatingExpenses = np.array([0, 0, 0, 0, 0, 0])
interestExpense = np.array([0, 0, 0, 0, 0, 0])
interestIncomeExpense = np.array([0, 0, 0, 0, 0, 0])
operatingIncomeLoss = np.array([0, 0, 0, 0, 0, 0])
netIncomeLoss = np.array([0, 0, 0, 0, 0, 0])
netProfitLoss = np.array([0, 0, 0, 0, 0, 0])
eps = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
epsDiluted = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
weightedAvgShares = np.array([0, 0, 0, 0, 0, 0])
weightedAvgSharesDiluted = np.array([0, 0, 0, 0, 0, 0])

CashStatmementDataFrame = pd.DataFrame({'Year': [2020, 2019, 2018, 2017, 2016, 2015]})
cashFromOperatingActivites = np.array([0, 0, 0, 0, 0, 0])
cashFromInvestingActivities = np.array([0, 0, 0, 0, 0, 0])
cashFromFinancingActivites = np.array([0, 0, 0, 0, 0, 0])


class BalanceSheetStorage():
    def __init__(self, year):
        self.year = year

    def printPandas():

        if(np.count_nonzero(cash) != 0 ):
            cash1 = cash.astype(int)
            BalanceSheetDataFrame['Cash/Cash Equiv'] = cash1
        if (np.count_nonzero(currentAssets) != 0):
            currentAssets1 = currentAssets.astype(int)
            BalanceSheetDataFrame['Current Assets'] = currentAssets1
        if (np.count_nonzero(currentLiabilities) != 0):
            currentLiabilities1 = currentLiabilities.astype(int)
            BalanceSheetDataFrame['Current Liabilities'] = currentLiabilities1
        if (np.count_nonzero(assets) != 0):
            assets1 = assets.astype(int)
            BalanceSheetDataFrame['Assets'] = assets1
        if (np.count_nonzero(lase) != 0):
            lase1 = lase.astype(int)
            BalanceSheetDataFrame['Liabilities and SE'] = lase1
        if (np.count_nonzero(stockholdersequity) != 0):
            stockholdersequity1 = stockholdersequity.astype(int)
            BalanceSheetDataFrame['Stockholders Equity'] = stockholdersequity1
        if (np.count_nonzero(accountsReceivable) != 0):
            accountsReceivable1 = accountsReceivable.astype(int)
            BalanceSheetDataFrame['Accounts Recievable'] = accountsReceivable1
        if (np.count_nonzero(accountsPayable) != 0):
            accountsPayable1 = accountsPayable.astype(int)
            BalanceSheetDataFrame['Accounts Payable'] = accountsPayable1
        if (np.count_nonzero(netInventory) != 0):
            netInventory1 = netInventory.astype(int)
            BalanceSheetDataFrame['Net Inventory'] = netInventory1
        if (np.count_nonzero(plantPropertyEq) != 0):
            plantPropertyEq1 = plantPropertyEq.astype(int)
            BalanceSheetDataFrame['Net Plant/Prop/Eq'] = plantPropertyEq1
        if (np.count_nonzero(accruedLiabilities) != 0):
            accruedLiabilities1 = accruedLiabilities.astype(int)
            BalanceSheetDataFrame['Accrued Liabilities'] = accruedLiabilities1
        if (np.count_nonzero(longTermDebt) != 0):
            longTermDebt1 = longTermDebt.astype(int)
            BalanceSheetDataFrame['Long Term Debt'] = longTermDebt1
        if (np.count_nonzero(retainedEarnings) != 0):
            retainedEarnings1 = retainedEarnings.astype(int)
            BalanceSheetDataFrame['Retained Earnings'] = retainedEarnings1
        if (np.count_nonzero(prepaidExpenses) != 0):
            prepaidExpenses1 = prepaidExpenses.astype(int)
            BalanceSheetDataFrame['Prepaid Expenses'] = prepaidExpenses1


        ##### INCOME STATEMENT ######
        if(np.count_nonzero(revenues) != 0):
            revenues1 = revenues.astype(int)
            IncomeStatementDataFrame['Revenues'] = revenues1
        if (np.count_nonzero(netRevenue) != 0):
            netRevenue1 = netRevenue.astype(int)
            IncomeStatementDataFrame['Net Revenue'] = netRevenue1
        if (np.count_nonzero(grossProfit) != 0):
            grossProfit1 = grossProfit.astype(int)
            IncomeStatementDataFrame['Gross Profit/Margin'] = grossProfit1
        if (np.count_nonzero(salesRevenue) != 0):
            salesRevenue1 = salesRevenue.astype(int)
            IncomeStatementDataFrame['Sales Revenue'] = salesRevenue1
        if (np.count_nonzero(costOfGoodsServicesSold) != 0):
            costOfGoodsServicesSold1 = costOfGoodsServicesSold.astype(int)
            IncomeStatementDataFrame['Cost Goods Sold'] = costOfGoodsServicesSold1
        if (np.count_nonzero(costOfRevenue) != 0):
            costOfRevenue1 = costOfRevenue.astype(int)
            IncomeStatementDataFrame['Cost Of Revenue'] = costOfRevenue1
        if (np.count_nonzero(costsAndExpense) != 0):
            costsAndExpense1 = costsAndExpense.astype(int)
            IncomeStatementDataFrame['Costs & Expenses'] = costsAndExpense1
        if (np.count_nonzero(operatingExpenses) != 0):
            operatingExpenses1 = operatingExpenses.astype(int)
            IncomeStatementDataFrame['Operating Expenses'] = operatingExpenses1
        if (np.count_nonzero(interestExpense) != 0):
            interestExpense1 = interestExpense.astype(int)
            IncomeStatementDataFrame['Interest Expense'] = interestExpense1
        if (np.count_nonzero(interestIncomeExpense) != 0):
            interestIncomeExpense1 = interestIncomeExpense.astype(int)
            IncomeStatementDataFrame['Interest Expenses'] = interestIncomeExpense1
        if (np.count_nonzero(operatingIncomeLoss) != 0):
            operatingIncomeLoss1 = operatingIncomeLoss.astype(int)
            IncomeStatementDataFrame['Operating Income/Loss'] = operatingIncomeLoss1
        if (np.count_nonzero(netIncomeLoss) != 0):
            netIncomeLoss1 = netIncomeLoss.astype(int)
            IncomeStatementDataFrame['Net Income/Loss'] = netIncomeLoss1
        if (np.count_nonzero(netProfitLoss) != 0):
            netProfitLoss1 = netProfitLoss.astype(int)
            IncomeStatementDataFrame['Net Profit/Loss'] = netProfitLoss1
        if (np.count_nonzero(eps) != 0):
            IncomeStatementDataFrame['EPS Basic'] = eps
        if (np.count_nonzero(epsDiluted) != 0):
            IncomeStatementDataFrame['EPS Diluted'] = epsDiluted
        if (np.count_nonzero(weightedAvgShares) != 0):
            weightedAvgShares1 = weightedAvgShares.astype(int)
            IncomeStatementDataFrame['Avg Shares Outstanding'] = weightedAvgShares1
        if (np.count_nonzero(weightedAvgSharesDiluted) != 0):
            weightedAvgSharesDiluted1 = weightedAvgSharesDiluted.astype(int)
            IncomeStatementDataFrame['Avg Shares Outstanding Diluted'] = weightedAvgSharesDiluted1


        ### Cash Flow Statement ###
        if (np.count_nonzero(cashFromOperatingActivites) != 0):
            CashStatmementDataFrame['Cash Operating Activities'] = cashFromOperatingActivites

        if (np.count_nonzero(cashFromInvestingActivities) != 0):
            CashStatmementDataFrame['Cash Investing Activities'] = cashFromInvestingActivities

        if (np.count_nonzero(cashFromFinancingActivites) != 0):
            CashStatmementDataFrame['Cash Financing Activities'] = cashFromFinancingActivites

        print(BalanceSheetDataFrame)
        print(IncomeStatementDataFrame)
        print(CashStatmementDataFrame)
        #ds = LiquidityDataFrame.T
        #print(ds)
        print(LiquidityDataFrame)
        print(ProfitibilityDataFrame)


    def create_csv(company_ticker):
        #BalanceSheetDataFrame.to_csv(company_ticker)
        #IncomeStatementDataFrame.to_csv(company_ticker)
        with open(company_ticker, 'w') as f:
            pd.concat([BalanceSheetDataFrame, IncomeStatementDataFrame, CashStatmementDataFrame], axis=1).to_csv(f)


    def liquidity(num):
        if (num == 1):
            Liquidity_Ratios.current_ratio(currentAssets,currentLiabilities)
            Liquidity_Ratios.working_capital(currentAssets,currentLiabilities)
            Liquidity_Ratios.cash_ratio(cash,currentLiabilities)
            Liquidity_Ratios.quick_ratio(currentAssets,netInventory,prepaidExpenses,currentLiabilities)
            Liquidity_Ratios.cash_debt_coverage(cashFromOperatingActivites,currentLiabilities)

            Profitibility_Ratios.gross_profit_margin(netRevenue,revenues,grossProfit)
            Profitibility_Ratios.net_margin(netRevenue,revenues,salesRevenue,netIncomeLoss)
            #Profitibility_Ratios.eps_regular(eps)
            #Profitibility_Ratios.eps_diluted(epsDiluted)
            #Profitibility_Ratios.return_on_assets(netIncomeLoss,assets)
            #Profitibility_Ratios.return_on_equity(netIncomeLoss,stockholdersequity)
            #Profitibility_Ratios.free_cash_flow(cashFromOperatingActivites,interestExpense,cashFromInvestingActivities)


    def find(xbrl_str,contextref,contextRefIncome, contextRefCash, YR):
        soup = BeautifulSoup(xbrl_str, 'lxml')
        tag_list = soup.find_all()
        #for tag in tag_list:
        for tag in tag_list:
            if ('us-gaap:cashandcashequivalentsatcarryingvalue' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:cashandcashequivalentsatcarryingvalue'):
                    x = tag.attrs['contextref']
                    cashTag = float(tag.text)
                    get_generic_year(x,cashTag,contextref,YR,cash)
            if ('us-gaap:assetscurrent' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:assetscurrent'):
                    currentAssetsTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,currentAssetsTag,contextref,YR,currentAssets)

            if ('us-gaap:liabilitiescurrent' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:liabilitiescurrent'):
                    currentLiabilitiesTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,currentLiabilitiesTag,contextref,YR,currentLiabilities)


            if ('us-gaap:assets' in tag.name):
                if(tag.text != '' and tag.name == 'us-gaap:assets'):
                    assetsTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,assetsTag,contextref,YR,assets)

            if ('us-gaap:liabilitiesandstockholdersequity' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:liabilitiesandstockholdersequity'):
                    x = tag.attrs['contextref']
                    LASETag = float(tag.text)
                    get_generic_year(x,LASETag,contextref,YR,lase)

            if ('us-gaap:stockholdersequity' in tag.name):
                if(tag.text != '' and tag.name == 'us-gaap:stockholdersequity'):
                    seTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,seTag,contextref,YR,stockholdersequity)

            if ('us-gaap:accountsreceivablenetcurrent' in tag.name):
                if(tag.text != '' and tag.name == 'us-gaap:accountsreceivablenetcurrent'):
                    arTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,arTag,contextref,YR,accountsReceivable)

            if ('us-gaap:accountspayablecurrent' in tag.name):
                if(tag.text != '' and tag.name == 'us-gaap:accountspayablecurrent'):
                    apTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,apTag,contextref,YR,accountsPayable)

            if ('us-gaap:inventorynet' in tag.name or
                    'us-gaap:inventoryfinishedgoodsnetofreserves' in tag.name or
                     'inventorynetofallowancescustomeradvancesandprogressbillings' in tag.name):
                if (tag.text != ''):
                    niTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,niTag,contextref,YR,netInventory)

            if ('us-gaap:propertyplantandequipmentnet' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:propertyplantandequipmentnet'):
                    ppeTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,ppeTag,contextref,YR,plantPropertyEq)

            if ('us-gaap:accruedliabilitiescurrent' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:accruedliabilitiescurrent'):
                    aclTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,aclTag,contextref,YR,accruedLiabilities)

            if ('us-gaap:retainedearningsaccumulateddeficit' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:retainedearningsaccumulateddeficit'):
                    reTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,reTag,contextref,YR,retainedEarnings)

            if ('us-gaap:longtermdebtnoncurrent' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:longtermdebtnoncurrent'):
                    ltdTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,ltdTag,contextref,YR,longTermDebt)

            if ('us-gaap:prepaidexpensecurrent' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:prepaidexpensecurrent'):
                    ppTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,ppTag,contextref,YR,prepaidExpenses)


            #### INCOME STATEMENT #####
            if ('us-gaap:revenuefromcontractwithcustomerexcludingassessedtax' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:revenuefromcontractwithcustomerexcludingassessedtax'):
                    netRevTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,netRevTag,contextRefIncome,YR,netRevenue)

            if ('us-gaap:grossprofit' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:grossprofit'):
                    gpTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,gpTag,contextRefIncome,YR,grossProfit)

            if ('us-gaap:revenues' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:revenues'):
                    revenuesTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,revenuesTag,contextRefIncome,YR,revenues)

            if ('us-gaap:salesrevenuegoodsnet' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:salesrevenuegoodsnet'):
                    srTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,srTag,contextRefIncome,YR,salesRevenue)

            if ('us-gaap:costofgoodsandservicessold' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:costofgoodsandservicessold'):
                    cogsTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,cogsTag,contextRefIncome,YR,costOfGoodsServicesSold)

            if ('us-gaap:costofrevenue' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:costofrevenue'):
                    corTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,corTag,contextRefIncome,YR,costOfRevenue)

            if ('us-gaap:costsandexpenses' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:costsandexpenses'):
                    caeTag = float(tag.text)
                    x = tag.attrs['contextref']
                    get_generic_year(x,caeTag,contextRefIncome,YR,costsAndExpense)

            if ('us-gaap:operatingexpenses' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:operatingexpenses'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,operatingExpenses)

            if ('us-gaap:interestexpense' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:interestexpense'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,interestExpense)

            if ('us-gaap:interestincomeexpensenonoperatingnet' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:interestincomeexpensenonoperatingnet'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,interestIncomeExpense)

            if ('us-gaap:operatingincomeloss' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:operatingincomeloss'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,operatingIncomeLoss)
            if ('us-gaap:netincomeloss' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:netincomeloss'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,netIncomeLoss)
            if ('us-gaap:profitloss' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:profitloss'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,netProfitLoss)

            if ('us-gaap:earningspersharebasic' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:earningspersharebasic'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,eps)

            if ('us-gaap:earningspersharediluted' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:earningspersharediluted'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,epsDiluted)

            if ('us-gaap:weightedaveragenumberofsharesoutstandingbasic' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:weightedaveragenumberofsharesoutstandingbasic'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,weightedAvgShares)

            if ('us-gaap:weightedaveragenumberofdilutedsharesoutstanding' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:weightedaveragenumberofdilutedsharesoutstanding'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefIncome,YR,weightedAvgSharesDiluted)


            #### Cash Statement #####

            if ('us-gaap:netcashprovidedbyusedinoperatingactivities' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:netcashprovidedbyusedinoperatingactivities'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefCash,YR,cashFromOperatingActivites)

            if ('us-gaap:netcashprovidedbyusedininvestingactivities' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:netcashprovidedbyusedininvestingactivities'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefCash,YR,cashFromInvestingActivities)

            if ('us-gaap:netcashprovidedbyusedinfinancingactivities' in tag.name):
                if (tag.text != '' and tag.name == 'us-gaap:netcashprovidedbyusedinfinancingactivities'):
                    x = tag.attrs['contextref']
                    get_generic_year(x,float(tag.text),contextRefCash,YR,cashFromFinancingActivites)


def get_generic_year(x,tag,contextRefIncome,YR,arraySend):
    if (x == 'FI2020Q4' or x == 'FI2020Q4YTD' or x == 'FD2020Q4YTD' or x == 'FD2020Q4'):
        store_generic_pandas(tag, 2020, arraySend)
    elif (x == 'FI2019Q4' or x == 'FI2019Q4YTD' or x == 'FD2019Q4YTD' or x == 'FD2019Q4'):
        store_generic_pandas(tag, 2019, arraySend)
    elif (x == 'FI2018Q4' or x == 'FI2018Q4YTD' or x == 'FD2018Q4YTD' or x == 'FD2018Q4'):
        store_generic_pandas(tag, 2018, arraySend)
    elif (x == 'FI2017Q4' or x == 'FI2017Q4YTD' or x == 'FD2017Q4YTD' or x == 'FD2017Q4'):
        store_generic_pandas(tag, 2017, arraySend)
    elif (x == 'FI2016Q4' or x == 'FI2016Q4YTD' or x == 'FD2016Q4YTD' or x == 'FD2016Q4'):
        store_generic_pandas(tag, 2016, arraySend)
    elif (x == 'FI2015Q4' or x == 'FI2015Q4YTD' or x == 'FD2015Q4YTD' or x == 'FD2015Q4'):
        store_generic_pandas(tag, 2015, arraySend)
    elif (x == contextRefIncome):
        store_generic_pandas(tag, YR, arraySend)

def store_generic_pandas(number, year, arr):
    if year == 2020:
        if arr[0] == 0:
            arr[0] = number
    elif year == 2019:
        if arr[1] == 0:
            arr[1] = number
    elif year == 2018:
        if arr[2] == 0:
            arr[2] = number
    elif year == 2017:
        if arr[3] == 0:
            arr[3] = number
    elif year == 2016:
        if arr[4] == 0:
            arr[4] = number
    elif year == 2015:
        if arr[5] == 0:
            arr[5] = number







