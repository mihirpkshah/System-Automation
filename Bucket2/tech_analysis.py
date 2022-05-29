from glob import glob
from random import random
import pandas as pd
indicesData = {} # {SYMBOL: dataFrame}
def start():
    # TODO: Clear Bucket2/stocks folder
    loadIndices(["NIFTY"]) # updated indicesData
    stockFileNames = list(glob("./Bucket1/stocks/*.csv"))
    stockFileNames = ["./Bucket1/stocks/ADANIPOWER.csv"]
    print("Total Stocks: ",len(stockFileNames))
    for stockFilename in stockFileNames[0:10]:
        df = pd.read_csv(stockFilename)
        if doTechAnalysis(df):
            # TODO: add this stock to Bucket2/stocks
            continue

# THIS CODE WILL BE UPDATED BY ROHAN
def doTechAnalysis(df: pd.DataFrame) -> bool:# df is complete stock data
    print(get52WeekHigh(df))
    getMovingAvg(df, 40) # 40 days => Series of len => df.len - 40
    return random() < 0.5

def get52WeekHigh(df: pd.DataFrame) -> pd.DataFrame:
    return df.tail(250).sort_values(by="High",ascending=False ).iloc[0]

def getMovingAvg(df: pd.DataFrame, days: int) -> pd.Series:
    return None
def loadIndices(indexList: list): # update data to indicesData
    return None
start()
