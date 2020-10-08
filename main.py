dateb = '20201001'
CIK = '0000789019'
form = '10-K'
company_ticker = 'msft'
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"

from companyInfo import GetCompanyInfo
from companyInfo import Get_URL
from companyInfo import Get_Data
from companyInfo import GET_XBRL
from bs4 import BeautifulSoup
import requests
import sys


if __name__ == '__main__':
    GetCompanyInfo(company_ticker, dateb, form)
    list = GetCompanyInfo.get_list(company_ticker)
    cik = GetCompanyInfo.get_cik(company_ticker,list)
    param_dict = {'CIK': cik,
                  'type': form,
                  'dateb':'20200913'}
    url = Get_URL.retrieve(endpoint,param_dict)
    #print(url)
    secLink = Get_Data.sift(url,'2020') #has to be before 2020
    #seems to get funked up with the iXBRL
    print(secLink)
    doc_str = Get_Data.getHTML(secLink)
    str = GET_XBRL.check(doc_str)
    GET_XBRL.find(str)

