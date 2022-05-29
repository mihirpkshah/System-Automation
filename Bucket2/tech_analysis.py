from datetime import datetime, timedelta
from fileinput import filename
from glob import glob
from random import random
from numpy import float64
import pandas as pd
from requests import head
import shutil
indicesData = {} # {SYMBOL: dataFrame}
def start():
    # TODO: Clear Bucket2/stocks folder
    loadIndices(["NIFTY"]) # updated indicesData
    stockFileNames = list(glob("./Bucket1/stocks/*.csv"))
    print("Total Stocks: ",len(stockFileNames))
    i=0
    with open("./Bucket2/subBucket2a.txt") as subBucket2a:
        for stockFilename in stockFileNames:
            try:
                df = read_csv(stockFilename)
                if doTechAnalysis_2a(df):
                    # TODO: add this stock to Bucket2/stocks
                    subBucket2a.write(stockFilename.split["/"][-1])
                    i+=1
            except Exception as e: continue
    print("Total",i,"stocks added to subBucket2a")
    
    with open("./Bucket2/subBucket2a.txt", "r") as subBucket2a:
        stocksToKeepIn2a = []
        for stockName in subBucket2a.readlines():
            stockFilename = "./Bucket1/stocks" + stockName
            try:
                df = read_csv(stockFilename)
                if doTechAnalysis_2b(df):
                    stocksToKeepIn2a.append(stockFilename.split["/"][-1])
                    # TODO: add this stock to Bucket2/stocks
                    i+=1
            except Exception as e: continue
    print("Total",i,"stocks added to subBucket2b")

def read_csv(stockFilename: str):
    df = pd.read_csv(stockFilename, skiprows=1, dtype={"Open": float64, "High": float64, "Low": float64, "Close": float64, "Traded Qty": float64, "Delivery Qty": float64})
    columns = ["Symbol", "Date", "Open", "High", "Low", "Close", "Volume", "Delivery"]
    if df.shape[1] == 9: columns.append("_")
    df.columns = columns
    df["Date"] = pd.to_datetime(df["Date"], format="%Y%m%d")
    df.sort_values(by="Date")
    return df

def doTechAnalysis_2b(df: pd.DataFrame):
    return

# THIS CODE WILL BE UPDATED BY ROHAN
def doTechAnalysis_2a(df: pd.DataFrame) -> bool:# df is complete stock data
    week52High: pd.Series = get52WeekHigh(df)
    if week52High.shape[0] != 0 and week52High["Date"] + timedelta(days=20) == getTodayDate():
        return True
    else:
        return False

def getTodayDate():
    #return datetime(datetime.now().year, datetime.now().month, datetime.now().day)
    return datetime(2022, 5, 19)

def get52WeekHigh(df: pd.DataFrame, endDt: datetime = getTodayDate()) -> pd.Series:
    delta = getTodayDate() - timedelta(days=250)
    df_subset: pd.DataFrame = df[df["Date"] >= delta].sort_values(by="High",ascending=False)
    if (df_subset.shape[0] == 0): return pd.Series(dtype=float64)
    return df[df["Date"] >= delta].sort_values(by="High",ascending=False).iloc[0]

def getVolAcc(df: pd.DataFrame, endDate: datetime = getTodayDate(), nDays: int = 250):
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
