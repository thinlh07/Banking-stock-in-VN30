# Banking stocks in VN30 
# Top 4 Biggest banks in Vietnam

### Introduction

The project aims to parse through banking stock data in VN30 index to give a past performance view of these stocks. Then, we will look into top 4 biggest banks in Vietnam to find out how each bank price impact on others.
  For achieving the aims, there are some questions will be answering: 
  1. What was the price movement of the stock? 
  2. What was the price moving average of top 4 biggest banks? 
  3. What was the daily return of top 4 biggest banks on average?
  4. What was the correlation between the top 4 biggest bank?
  5. For each expected return value, how much risk we incur in a particular stock?

  Some keywords should be known:
  1. VN30 index [LINK](https://en.wikipedia.org/wiki/VN30_Equal_Weight_Index)
  2. Moving Average [LINK](https://www.investopedia.com/terms/m/movingaverage.asp)
  3. Correlation [LINK](https://www.jmp.com/en_ca/statistics-knowledge-portal/what-is-correlation.html#:~:text=Correlation%20is%20a%20statistical%20measure,statement%20about%20cause%20and%20effect.)

### Data Source and Integrity 
  In context of this work, the data was taken from Yahoo Finance, which is a trust financial data source. 
 
### Outcomes 
  First, we can take a quick look at the price movement of all banking stocks in VN30 historically. 
  ![closing_price.png](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/closing_price.png)

  Through out the project, there are some key values: 
   1. Generally, all banks have experieced an uptrend over the time, especially TCB owning the most stable rise. Meanwhile, STB, TPB, VPB are three banks with highest level of fluctation.
   2. The moving average of 10 days, 20 days are closer to the stock price than the moving average of 50 days, so they probably more useful for analysing the stock in the short time.
   3. Within top 4 banks, only BID's histogram is left-skewed that means the stock has the largest frequency of positive daily return.
   4. The returns and prices of these stocks tend to move in the same direction.

![Moving Average](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/Moving%20average.png)
![Daily Return](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/Daily%20Return.png)
![Correlation](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/Correlation.png)
![Daily Return](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/Daily%20Return%20Histogram.png)

A quick look into the risk and expected return relationship of the four biggest banks:
![Risk - Expected Return](https://github.com/thinlh07/Banking-stock-in-VN30/blob/main/Risk%20-%20Expected%20Return.png)
