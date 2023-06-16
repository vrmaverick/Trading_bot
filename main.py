# region imports
from AlgorithmImports import *
# endregion

class CasualSkyBlueRabbit(QCAlgorithm):

    def Initialize(self): #called everytime a tick event occurs or bar reaches end time
        self.SetStartDate(2022, 1, 1)
        self.SetEndDate(2023,1,1)
        self.SetCash(100000)  # Set Strategy Cash #just for testing
        spy = self.AddEquity("SPY",Resolution.Daily)#daily data
        #AddForex()
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.spy = spy.Symbol #to get more info than tickers
        self.SetBenchmark("SPY")#actual index

        self.entryprice = 0
        self.period = timedelta(31) #31 days frame
        self.nextEntryTime = self.Time#start right away


    def OnData(self, data: Slice): #calle everytime  end of bar is reached or tick is over
        #slice class provides symbol value and time info
        # price = data.Bars[self.spy].Close #close price of day before
        price = data[self.spy].Close #close price of day before
