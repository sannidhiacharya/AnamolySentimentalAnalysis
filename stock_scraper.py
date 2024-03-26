import pandas as pd
import csv
import time
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_rows", None)

class StockScrape:
    def scraper(self, file_name):
        self.df1 = pd.read_csv('https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_csv/data/3c88fab8ec158c3cd55145243fe5fcdf/nyse-listed_csv.csv')
        self.df2 = pd.read_json('https://www.sec.gov/files/company_tickers.json')

        csv_data = []
        
        for key, entry in self.df2.items():
            ticker = entry.get("ticker")
            title = entry.get("title")
    
            if ticker is not None and title is not None:
                csv_data.append([ticker, title])

        self.df3 = pd.DataFrame(csv_data)
        self.df3 = self.df3.rename(columns={0: 'ACT Symbol',1: 'Company Name'})
        
        self.df1 = pd.concat([self.df1, self.df3], ignore_index=True)
        self.df1 = self.df1.iloc[:, 0]
        self.df1 = self.df1.drop_duplicates(subset='ACT Symbol')

        output_path = os.path.join(os.getcwd(), file_name)
        print("Stocks downloaded at ", time.time())


