from companyInfo import GetCompanyInfo
from companyInfo import Get_URL
from companyInfo import Get_Data
from companyInfo import GET_XBRL
from balanceSheet import BalanceSheetStorage
from contextRefId import retrieve
from contextRefId import retrieveYear
from contextRefId import retrieveIncome
from contextRefId import retrieveCash
from datetime import date
from tqdm import tqdm



today = date.today()
currentDate = today.strftime("%Y%m%d")
currentYearString = today.strftime("%Y")
form = '10-K'
company_ticker = 'mu'
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"


if __name__ == '__main__':
    GetCompanyInfo(company_ticker, currentDate, form)
    list = GetCompanyInfo.get_list(company_ticker)
    cik = GetCompanyInfo.get_cik(company_ticker,list)
    param_dict = {'CIK': cik,
                  'type': form,
                  'dateb': currentDate}
    url = Get_URL.retrieve(endpoint,param_dict)

    currentYear = Get_Data.findYearPartTwo(url,currentYearString)
    currentYearPeriodForSheets = currentYear

    currentYearString = str(currentYear)
    secLink1 = Get_Data.sift(url,currentYearString)

    currentYear = currentYear - 1
    currentYearString = str(currentYear)
    secLink2 = Get_Data.sift(url,currentYearString)

    currentYear = currentYear - 1
    currentYearString = str(currentYear)
    secLink3 = Get_Data.sift(url, currentYearString)

    currentYear = currentYear - 1
    currentYearString = str(currentYear)
    secLink4 = Get_Data.sift(url, currentYearString)

    for i in range(4):
        if (i == 0):
            doc_str1 = Get_Data.getHTML(secLink1)
        elif (i == 1):
            doc_str2 = Get_Data.getHTML(secLink2)
        elif (i == 2):
            doc_str3 = Get_Data.getHTML(secLink3)
        elif (i == 3):
            doc_str4 = Get_Data.getHTML(secLink4)

    str1 = GET_XBRL.check(doc_str1)
    str2 = GET_XBRL.check(doc_str2)
    str3 = GET_XBRL.check(doc_str3)
    str4 = GET_XBRL.check(doc_str4)

    for i in tqdm(range(4)):
        if(i == 0):
            contextRef1 = retrieve(str1)
        elif(i==1):
            contextRef2 = retrieve(str2)
        elif(i==2):
            contextRef3 = retrieve(str3)
        elif(i==3):
            contextRef4 = retrieve(str4)

    for i in tqdm(range(4)):
        if(i == 0):
            contextRefIncome1 = retrieveIncome(str1)
        elif(i==1):
            contextRefIncome2 = retrieveIncome(str2)
        elif(i==2):
            contextRefIncome3 = retrieveIncome(str3)
        elif(i==3):
            contextRefIncome4 = retrieveIncome(str4)

    for i in tqdm(range(4)):
        if(i == 0):
            contextRefCash1 = retrieveCash(str1)
        elif(i==1):
            contextRefCash2 = retrieveCash(str2)
        elif(i==2):
            contextRefCash3 = retrieveCash(str3)
        elif(i==3):
            contextRefCash4 = retrieveCash(str4)


    for i in tqdm(range(4)):
        if(i == 0):
            year1 = retrieveYear(str1)
            year1 = int(year1)
        elif(i==1):
            year2 = retrieveYear(str2)
            year2 = int(year2)
        elif(i==2):
            year3 = retrieveYear(str3)
            year3 = int(year3)
        elif(i==3):
            year4 = retrieveYear(str4)
            year4 = int(year4)


    for i in tqdm(range(4)):
        if(i == 0):
            BalanceSheetStorage.find(str1, contextRef1, contextRefIncome1, contextRefCash1, year1)
        elif(i==1):
            BalanceSheetStorage.find(str2, contextRef2, contextRefIncome2, contextRefCash2, year2)
        elif (i == 2):
            BalanceSheetStorage.find(str3, contextRef3, contextRefIncome3, contextRefCash3, year3)
        elif (i == 3):
            BalanceSheetStorage.find(str4, contextRef4,contextRefIncome4, contextRefCash4, year4)

    BalanceSheetStorage.liquidity(1)
    BalanceSheetStorage.printPandas()
    #BalanceSheetStorage.create_xlsx(company_ticker)




