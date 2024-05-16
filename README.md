# Banking stocks in VN30 
# Top 4 Biggest banks in Vietnam

### Introduction, Value and Inspiration
  In this project, the author aims to parse through banking stock data in VN30 index to generate meaningful insights and 
  visualise the relationship between top 4 biggest banks. This probably give a vie



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
  ![closing_price.png](/Users/huuthinle/Documents/Banking-stock-in-VN30/closing_price.png)








  
  The most important value in this project came from deriving the Z-Value for respective tenors (e.g. 1y3y or 3y5y). This is how a spread trade makes money so it's important to know whether the curve has move with or against our favours in selected timeframes (7 days, 14 days and 1 month). The steps to derive these viz are: 
  1. Create a simple matrix calculation the spreads between all tenors
  2. Calculate the mean and standard deviation to use in the formula (z = (x-m)/u) 
  3. Visualise using seaborn and applying heatmap gradient to help with quick spotting 

  Example intepretation (7 days rolling): 3s5s moved by 2 Z's meaning spread has widened compared to historical average. This means that the curve has steepend.

  ![7 days](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/7d_rolling.png) 
  ![14 days](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/14d_rolling.png)
  ![1_month](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/1mo_rolling.png) 
