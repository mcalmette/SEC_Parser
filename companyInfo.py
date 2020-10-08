from bs4 import BeautifulSoup
import requests
import sys
import datefinder
endpoint = r"https://www.sec.gov/cgi-bin/browse-edgar"
#pip install lxml
#pip install beautifulsoup4
#pip install python-xbrl
#pip install xmlschema
#pip install datefinder


class GetCompanyInfo:
    def __init__(self,ticker,dateb, form):
        self.ticker = ticker
        self.dateb = dateb
        self.form = form

    def get_list(ticker):
        listFind = ''
        ch = len(ticker)
        if ch == 1:
            listFind = 'oneLetter'
        elif ch == 2:
            listFind = 'twoLetter'
        elif ch == 3:
            listFind = 'threeLetter'
        elif ch == 4:
            listFind = 'fourLetter'
        else:
            listFind = 'elseLetter'

        return listFind

    def get_cik(ticker, listFind):
        cikArray = []

        with open(listFind, 'r') as f:
            for line in f:
                if ticker in line:
                    lineArray = line
                    stringLength = len(lineArray)
                    for x in range(0,stringLength):
                        if lineArray[x].isdigit() == True:
                            cikArray.append(lineArray[x])
                    cikInt = ''.join(str(e) for e in cikArray)
                    return cikInt
        print("Ticker not found, aborting program.")
        return 000
        #need to quit program

    def get_dateb(self):
        return self.dateb

    def get_form(self):
        return self.form


class Get_URL():
    def retrieve(endpoint,param_dict):
        doc_link = ''
        response = requests.get(url=endpoint, params=param_dict)
        print(response.url)
        return response


class Get_Data():
    def sift(response,year):
        soup = BeautifulSoup(response.content, 'html.parser')
        table_tag = soup.find('table', class_='tableFile2')
        rows = table_tag.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 3:
                if year in cells[3].text:
                    doc_link = 'https://www.sec.gov' + cells[1].a['href']
        # Exit if document link couldn't be found
        if doc_link == '':
            print("Couldn't find the document link")
            sys.exit()
        return doc_link

    def getHTML(doc_link):
        # Obtain HTML for document page
        doc_resp = requests.get(doc_link)
        doc_str = doc_resp.text
        return doc_str

class GET_XBRL():
    def check(doc_str):
        # Find the XBRL link
        xbrl_link = ''
        soup = BeautifulSoup(doc_str, 'html.parser')
        table_tag = soup.find('table', class_='tableFile', summary='Data Files')
        rows = table_tag.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 3:
                if 'INS' in cells[3].text:
                    xbrl_link = 'https://www.sec.gov' + cells[2].a['href']
                elif 'XML' in cells[3].text:
                    xbrl_link = 'https://www.sec.gov' + cells[2].a['href']


        # Obtain XBRL text from document
        xbrl_resp = requests.get(xbrl_link)
        xbrl_str = xbrl_resp.text
        print(xbrl_link)
        return xbrl_str

    def test_other_method(doc_str):
        print("test")
        #ITS the INS


    def find(xbrl_str):
        # Find and print stockholder's equity
        soup = BeautifulSoup(xbrl_str, 'lxml')
        tag_list = soup.find_all()
        for tag in tag_list: #need to figure out the list
            if tag.name == 'us-gaap:liabilities':
                x = tag.attrs['contextref']
                #print(x)
                # class to figure out string length
                #year = x[2] + x[3] + x[4] + x[5]
                #month = x[7] + x[8]
                #day = x[10] + x[11]
                # month = "S"
                # day = "s"
                #print(tag)
                print(tag.attrs['contextref'] + " Liabilities: " + tag.text)
                number = int(tag.text)
                number = number / 1000
                #print(number)
                #Store_Date.store(year, month, day, tag.text)
                #input_string = tag.attrs['contextref']
                #matches = list(datefinder.find_dates(input_string))
                #if len(matches) > 0:
                    # date returned will be a datetime.datetime object. here we are only using the first match.
                    #date = matches[0]
                    #print(date)
                #else:
                    #print('No dates found')