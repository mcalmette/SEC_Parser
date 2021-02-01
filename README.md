# SEC_Parser

![alt text](https://forthebadge.com/images/badges/made-with-python.svg) ![alt text](https://forthebadge.com/images/badges/powered-by-coffee.svg)

## Usage: Python 3

## Libraries Installations
```
pip install lxml
pip install beautifulsoup4
pip install python-xbrl
pip install xmlschema
pip install pandas
pip install tqdm
pip install numpy

```

## About
Program was designed and built to quickly parse and store 10-K and 10-Q financial data from the SEC website. By using any stock ticker, the program searches for the company central index key housed in the letter files. With the param dictionary with company ticker, filing type, and date, it searches and stores with type 'XML'. The XML files are stored and parsed using Beautiful Soup's lxml for key values in the balance sheet, income statement, and cash flow statement. Using a pandas dataframe, different liquidity, solvency and profitibility ratios are performed. These are converted into an excel file which is placed in the project folder.


Note: Amended reports do not contain proper data and the program will terminate. 

## Stock Ticker
<img width="529" alt="Screen Shot 2021-01-31 at 10 12 13 PM" src="https://user-images.githubusercontent.com/56742122/106423132-ae389780-6414-11eb-99df-d4cb600a4984.png">
