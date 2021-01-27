from bs4 import BeautifulSoup
from datetime import datetime

def retrieve(xbrl_str):
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all()
    for tag in tag_list:
        if ('us-gaap:liabilitiesandstockholdersequity' in tag.name):
            x = (tag['contextref'])
            return x
    return 0

def retrieveIncome(xbrl_str):
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all()
    for tag in tag_list:
        if ('us-gaap:earningspersharebasic' in tag.name):
            if(tag.name == 'us-gaap:earningspersharebasic'):
                x = (tag['contextref'])
                return x
    return 0

def retrieveCash(xbrl_str):
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all()
    for tag in tag_list:
        if ('us-gaap:netcashprovidedbyusedininvestingactivities' in tag.name):
            if(tag.name == 'us-gaap:netcashprovidedbyusedininvestingactivities'):
                x = (tag['contextref'])
                return x
    return 0


def retrieveYear(xbrl_str):
    soup = BeautifulSoup(xbrl_str, 'lxml')
    tag_list = soup.find_all()
    for tag in tag_list:
        if ('dei:documentperiodenddate' in tag.name):
            if(tag.name == 'dei:documentperiodenddate'):
                x = tag.text
                dt = datetime.strptime(x, '%Y-%m-%d')
                return dt.year

#dei:documentperiodenddate

