from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import numpy as np

IncomeStatementDataFrame = pd.DataFrame({'Year': [2020, 2019, 2018, 2017, 2016, 2015]})

listForVars = 0

class IncomeStatementStorage():

    def print_bs(self):
        print("x")
        print()
