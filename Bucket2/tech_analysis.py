from datetime import datetime
from glob import glob
from random import random
import pandas as pd
indicesData = {} # {SYMBOL: dataFrame}
def start():
    # TODO: Clear Bucket2/stocks folder
    loadIndices(["NIFTY"]) # updated indicesData
    stockFileNames = list(glob("./Bucket1/stocks/*.csv"))
    stockFileNames = ["./Bucket1/stocks/GOLDTECH.csv"]
    print("Total Stocks: ",len(stockFileNames))
    for stockFilename in stockFileNames[0:10]:
        df = pd.read_csv(stockFilename)
        df.columns = ["Symbol", "Date", "Open", "High", "Low", "Close", "Volume", "Delivery"]
        df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
        df.sort_values(by="Date")
        if doTechAnalysis(df):
            # TODO: add this stock to Bucket2/stocks
            continue

# THIS CODE WILL BE UPDATED BY ROHAN
def doTechAnalysis(df: pd.DataFrame) -> bool:# df is complete stock data
    print(getVolAcc(df))
    getMovingAvg(df, 40) # 40 days => Series of len => df.len - 40
    return random() < 0.5

def get52WeekHigh(df: pd.DataFrame) -> pd.DataFrame:
    return df.tail(250).sort_values(by="High",ascending=False ).iloc[0]

def getVolAcc(df: pd.DataFrame, endDate: datetime = datetime.now(), nDays: int = 250):
    df_subset: pd.DataFrame = df[df["Date"] <= endDate].tail(nDays)
    df_subset.reset_index(inplace = True, drop = True)
    volAcc: float = 0
    print(df_subset)
    for index, row in df_subset.iterrows():
        if index == 0: continue
        if df_subset.iloc[index-1]["Close"] < row["Close"]:
            volAcc += row["Volume"]
        elif df_subset.iloc[index-1]["Close"] > row["Close"]:
            volAcc -= row["Volume"]
    return volAcc

def getMovingAvg(df: pd.DataFrame, days: int) -> pd.Series:
    return None
def loadIndices(indexList: list): # update data to indicesData
    return None
start()
