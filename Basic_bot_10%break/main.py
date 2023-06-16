# region imports
from AlgorithmImports import *
# endregion

class CasualSkyBlueRabbit(QCAlgorithm):

    def Initialize(self): #called everytime a tick event occurs or bar reaches end time
        self.SetStartDate(2021, 1, 1)
        self.SetEndDate(2022,1,1)
        self.SetCash(100000)  # Set Strategy Cash #just for testing
        spy = self.AddEquity("SPY",Resolution.Daily)#daily data
        #AddForex()
        spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        self.spy = spy.Symbol #to get more info than tickers
        self.SetBenchmark("SPY")#actual index

        self.entryPrice = 0
        self.period = timedelta(31) #31 days frame
        self.nextEntryTime = self.Time#start right away


    def OnData(self, data: Slice): #calle everytime  end of bar is reached or tick is over
        if not self.spy in data:
            return
        #slice class provides symbol value and time info
        # price = data.Bars[self.spy].Close #close price of day before
        price = data[self.spy].Close #close price of day before
        if not self.Portfolio.Invested: #arent invested??
            if self.nextEntryTime <= self.Time:
                self.SetHoldings(self.spy,1)#100% of our portfolio
                # self.MarketOrder(self.spy,int(self.Portfolio.Cash/price))#sends market order to specified symbol and quantity which can be -ve
                self.Log('buy spy #'+ str(price)) #signal in log
                self.entryPrice = price
        elif self.entryPrice*1.1<price or self.entryPrice*0.9>price:#exit code thresholds 10%
            self.Liquidate() #sell
            self.Log('sell spy #'+str(price))
            self.nextEntryTime = self.Time + self.period #deactivate for 30 days


