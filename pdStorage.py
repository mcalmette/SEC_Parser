from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
import sys
import pandas_read_xml as pdx
#from pdStorage import Pandas_Data_Frame
import xml.etree.ElementTree as ET
from lxml import etree
import re
import pandas as pd
import numpy as np

df = pd.DataFrame({'context':[2020,2019,2018,2017,2016,2015]})
revenues = [0,0,0,0,0,0]
cgs = [0,0,0,0,0,0]
grossprofit = [0,0,0,0,0,0]
marketingadvertising = [0,0,0,0,0,0]
adminexpense = [0,0,0,0,0,0]
liabilities = [0,0,0,0,0,]


class Store_data():
    def __init__(self, year):
        self.year = year

    def store(tag):
        x = tag.attrs['contextref']

    def find(xbrl_str):
        # Find and print stockholder's equity
        #print(xbrl_str)
        soup = BeautifulSoup(xbrl_str, 'lxml')
        tag_list = soup.find_all()
        #k = soup.find_all(text=re.compile("context id"))
        #mytree = ET.parse(xbrl_str)
        #root = etree.fromstring(xbrl_str)
        for tag in tag_list:
            if('us-gaap:revenuefromcontractwithcustomerexcludingassessedtax' in tag.name):
                if(tag.attrs['contextref'] == "FD2020Q4YTD"):
                    number = int(tag.text)
                    store_revenue_pandas(number,2020)
                elif (tag.attrs['contextref'] == "FD2019Q4YTD"):
                    number = int(tag.text)
                    store_revenue_pandas(number, 2019)
                elif (tag.attrs['contextref'] == "FD2018Q4YTD"):
                    number = int(tag.text)
                    store_revenue_pandas(number, 2018)
                elif (tag.attrs['contextref'] == "FD2017Q4YTD"):
                    number = int(tag.text)
                    store_revenue_pandas(number, 2017)

            if('us-gaap:costofgoodsandservicessold' in tag.name):
                costnum = int(tag.text)
                if (tag.attrs['contextref'] == "FD2020Q4YTD"):
                    store_cgs_pandas(costnum, 2020)
                elif (tag.attrs['contextref'] == "FD2019Q4YTD"):
                    store_cgs_pandas(costnum, 2019)
                elif (tag.attrs['contextref'] == "FD2018Q4YTD"):
                    store_cgs_pandas(costnum, 2018)
                elif (tag.attrs['contextref'] == "FD2017Q4YTD"):
                    store_cgs_pandas(costnum, 2017)

            if ('us-gaap:grossprofit' in tag.name):
                gp = int(tag.text)
                if (tag.attrs['contextref'] == "FD2020Q4YTD"):
                    store_grossprofit_pandas(gp, 2020)
                elif (tag.attrs['contextref'] == "FD2019Q4YTD"):
                    store_grossprofit_pandas(gp, 2019)
                elif (tag.attrs['contextref'] == "FD2018Q4YTD"):
                    store_grossprofit_pandas(gp, 2018)
                elif (tag.attrs['contextref'] == "FD2017Q4YTD"):
                    store_grossprofit_pandas(gp, 2017)

            if ('us-gaap:marketingandadvertisingexpense' in tag.name):
                mae = int(tag.text)
                if (tag.attrs['contextref'] == "FD2020Q4YTD"):
                    store_marketingadvertisement_expense(mae,2020)
                elif (tag.attrs['contextref'] == "FD2019Q4YTD"):
                    store_marketingadvertisement_expense(mae, 2019)
                elif (tag.attrs['contextref'] == "FD2018Q4YTD"):
                    store_marketingadvertisement_expense(mae, 2018)
                elif (tag.attrs['contextref'] == "FD2017Q4YTD"):
                    store_marketingadvertisement_expense(mae, 2017)

            if ('us-gaap:generalandadministrativeexpense' in tag.name):
                gae = int(tag.text)
                if (tag.attrs['contextref'] == "FD2020Q4YTD"):
                    store_admin_expense(gae,2020)
                elif (tag.attrs['contextref'] == "FD2019Q4YTD"):
                    store_admin_expense(gae, 2019)
                elif (tag.attrs['contextref'] == "FD2018Q4YTD"):
                    store_admin_expense(gae, 2018)
                elif (tag.attrs['contextref'] == "FD2017Q4YTD"):
                    store_admin_expense(gae, 2017)


        df['Revenue'] = revenues
        df['Cost Goods/Services'] = cgs
        df['Gross Proft'] = grossprofit
        #df['Marketing/Ad Expense'] = marketingadvertising
        #df['General Expense'] = adminexpense
        #print(df['General Expense'])
        print(df)
        #return df, turn into csv
        #then make graphs




def store_revenue_pandas(number,year):
    if year == 2020:
        revenues[0] = number
    elif year == 2019:
        revenues[1] = number
    elif year == 2018:
        revenues[2] = number
    elif year == 2017:
        revenues[3] = number
    elif year == 2016:
        revenues[4] = number

def store_cgs_pandas(number,year):
    if year == 2020:
        cgs[0] = number
    elif year == 2019:
        cgs[1] = number
    elif year == 2018:
        cgs[2] = number
    elif year == 2017:
        cgs[3] = number
    elif year == 2016:
        cgs[4] = number

def store_grossprofit_pandas(number,year):
    if year == 2020:
        grossprofit[0] = number
    elif year == 2019:
        grossprofit[1] = number
    elif year == 2018:
        grossprofit[2] = number
    elif year == 2017:
        grossprofit[3] = number
    elif year == 2016:
        grossprofit[4] = number

def store_marketingadvertisement_expense(number,year):
    if year == 2020:
        marketingadvertising[0] = number
    elif year == 2019:
        marketingadvertising[1] = number
    elif year == 2018:
        marketingadvertising[2] = number
    elif year == 2017:
        marketingadvertising[3] = number
    elif year == 2016:
        marketingadvertising[4] = number

def store_admin_expense(number,year):
    if year == 2020:
        adminexpense[0] = number
    elif year == 2019:
        adminexpense[1] = number
    elif year == 2018:
        adminexpense[2] = number
    elif year == 2017:
        adminexpense[3] = number
    elif year == 2016:
        adminexpense[4] = number











#store by making a new df and adding to existing context one
#revenues=[....]
#df['revenue']=revenues

#print(tag)
#print(tag.attrs['contextref'] + " assets: " + tag.text)

#yearS = [2020,2019,2018,2017,2016]
#plt.bar(yearS,revenues)
#plt.show()




