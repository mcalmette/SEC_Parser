# SEC_Parser

![alt text](https://forthebadge.com/images/badges/made-with-python.svg) 

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

## Specification
In main.py, enter the stock ticker and the file type (10-K or 10-Q). A false transpose will have values horizontally saved in excel file (see end screenshot for difference).

<img width="330" alt="Screen Shot 2021-01-31 at 10 51 33 PM" src="https://user-images.githubusercontent.com/56742122/106424377-eb058e00-6416-11eb-8f1f-26b5c5f8f76d.png">

The program prints out the link to the SEC website with EDGAR's search results housing the documentation. The following are links to the 10-K XML files.

![ezgif com-gif-maker](https://user-images.githubusercontent.com/56742122/106427380-1c348d00-641c-11eb-843f-f62988727df0.gif)


After running, an xlsx file will be created in the project file with the ticker as the file name. This can be opened either in the IDE or in the project folder.

![apple_gif](https://user-images.githubusercontent.com/56742122/106561512-aa247c80-64dd-11eb-9798-b80086ce54ac.gif)


## Ratios 
List of calculations and definitions for ratio analysis. 

![Ratio Derivations](https://github.com/mcalmette/SEC_Parser/blob/master/Ratios.md)

## Technical Analysis
![Technical Analysis](https://github.com/mcalmette/TechnicalAnalysis)
