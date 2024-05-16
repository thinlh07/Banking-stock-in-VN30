import pandas as pd
import numpy as np
import yfinance as yfinance
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_datareader as pdr
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

#Set up the investigating time.
end = dt.datetime.now()
start = dt.datetime(2024,1,1)

#The bank stocks used in the analysis
bank_list= ["ACB.VN", "BID.VN", "CTG.VN", "AGR.VN",
             "MBB.VN","SHB.VN", "STB.VN", 
             "TCB.VN", "TPB.VN","VCB.VN","VIB.VN", "VPB.VN"]
bank_data = yf.download(bank_list, start = start)
bank_data

# Checking for missing values
missing_data = bank_data.isnull().sum()
missing_percentage = (missing_data/ len(bank_data)) * 100
missing_info = pd.DataFrame({'Count': missing_data, 'Percentage': missing_percentage})
print("Missing Data Information:")
print(missing_info)

# Checking for unique values in each column to understand the data better
print("\nUnique Values Information:")
for column in bank_data.columns:
    print(f"{column}: {bank_data[column].nunique()} unique values")
  
#Summary stats
bank_data.describe()
#general info
bank_data.info()


# 1. What was the price movement of the stock?
closing_price= bank_data['Adj Close']
plt.figure (figsize = (20,30))
plt.subplots_adjust(top=1.25, bottom=1.2)

## Closing Price 
for i, ticker in enumerate (closing_price.columns,1):
    ticker_title = ticker.replace ('.VN', '')
    plt.subplot(4,3, i)
    plt.plot(bank_data.index, closing_price[ticker])

    plt.xticks(rotation = 45)
    plt.ylabel('Adj Close (VND)')
    plt.xlabel('Date')
    plt.title(f'Closing Price of {ticker_title}', weight = 'bold', fontsize = 40)
plt.tight_layout()


### Volume of Transaction
## Value Simplification.
bank_volume = bank_data['Volume']/1000000
bank_volume 
# Let's visulise the trading volume of each bank stock.
plt.figure (figsize = (30,40))
plt.subplots_adjust(top=1.25, bottom=1.2)

for i, ticker in enumerate (bank_volume.columns,1):
    ticker_title = ticker.replace ('.VN', '')
    plt.subplot(4,3, i)
    plt.plot(bank_volume.index, bank_volume[ticker])

    plt.xticks(rotation = 45)
    plt.ylabel('Volume (million)', fontsize = 25)
    plt.xlabel('Date', fontsize = 25)
    plt.title(f'Transaction Volume of {ticker_title}', weight = 'bold', fontsize = 40)
plt.tight_layout()
plt.show()

# 2. What was the price moving average of top 4 biggest banks?
top_bank = ['VCB.VN', 'AGR.VN', 'BID.VN', 'CTG.VN']
top_bank_price = closing_price[top_bank]
top_bank_price
ma_days = [10, 20, 50]

for ticker in top_bank_price.columns:
    for ma in ma_days:
        column_name = f"MA_{ma}_of_{ticker}"
        top_bank_price[column_name] = top_bank_price[ticker].rolling(window=ma).mean()
        
print(top_bank_price.tail())
# Let's plot moving average of top 4 bank stocks
fig, ax = plt.subplots (2,2,figsize = (20,10), )
 

#Vietcombank: MA_10, MA_20, MA_
top_bank_price[['VCB.VN','MA_10_of_VCB.VN','MA_20_of_VCB.VN','MA_50_of_VCB.VN']].plot(ax = ax[0,0])
ax[0,0].legend(title='', loc= 'best')
ax[0,0].set_title ('Vietcombank (VCB)', weight = 'bold')



#BIDV: MA_10, MA_20, MA_50
top_bank_price[['BID.VN','MA_10_of_BID.VN','MA_20_of_BID.VN','MA_50_of_BID.VN']].plot (ax = ax[0,1])
ax[0,1].set_title('BIDV (BID)', weight = 'bold')
ax[0,1].legend(title='', loc= 'lower right')

#Agribank MA_10, MA_20, MA_5

top_bank_price[['AGR.VN','MA_10_of_AGR.VN','MA_20_of_AGR.VN','MA_50_of_AGR.VN']].plot (ax = ax[1,0])
ax[1,0].set_title('Agribank (AGR', weight = 'bold')
ax[1,0].legend(title='', loc= 'best')

#Vietcombank: MA_10, MA_20, MA_50
top_bank_price[['CTG.VN','MA_10_of_CTG.VN','MA_20_of_CTG.VN','MA_50_of_CTG.VN']].plot (ax = ax[1,1])
ax[1,1].set_title('Vietinbank (CTG)', weight = 'bold')
ax[1,1].legend(title='', loc ='best')

plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# 3. What was the daily return of top 4 biggest banks on average?
top_bank = ['VCB.VN', 'AGR.VN', 'BID.VN', 'CTG.VN']
top_4_bank = closing_price[top_bank]
top_4_bank
# pct_change() used to find out the percent change of each stock on a daily basis
bank_change= {}
for bank in top_4_bank.columns:
    bank_change[bank] = top_4_bank[bank].pct_change()

# Let's plot the daily return percentage using for loop
plt.figure(figsize = (20,10))
for i, bank in enumerate (bank_change, 1):
    plt.subplot(2,2,i)
    bank_change[bank].plot(legend = True, linestyle = '--', marker ='o')
    plt.xlabel('Date')
    plt.ylabel ('Daily Return')
    plt.title (bank)

plt.suptitle('Daily Return of Top Banks', fontsize = 35, weight = 'bold')
plt.tight_layout()
plt.show()x
# How it look in histogram?
plt.figure(figsize=(12, 9))
for i, bank in enumerate (bank_change, 1):
    plt.subplot(2,2,i)
    bank_change[bank].hist(legend = True)
    plt.xlabel('Daily Return')
    plt.ylabel ('Frequency')
    plt.title (bank)
    
plt.tight_layout()
plt.show()


## 4. What was the correlation between the top 4 biggest bank ?
top_4_bank = ['VCB.VN', 'BID.VN', 'AGR.VN', 'CTG.VN']
closing_price = yf.download(top_4_bank, start = start)['Adj Close']
daily_return = closing_price.pct_change()
daily_return.head()
# Set up the figure based on the daiyly_return Data Frame
return_fig= sns.PairGrid(daily_return)

# map_upper, map_lower, and map_diag are parameters used to specify the types of plots displayed in different sections of a matrix plot:
return_fig.map_upper(sns.kdeplot, cmap='viridis')
return_fig.map_lower(plt.scatter, color = 'green')
return_fig.map_diag(plt.hist, bins = 20)
plt.figure(figsize = (15,10))
plt.subplot(2,2,1)
sns.heatmap(daily_return.corr(), annot = True, cmap= 'coolwarm', center = 0, vmin= -1, vmax = 1)
plt.title('Correlation of Daily Return')

plt.subplot(2,2,2)
sns.heatmap(closing_price.corr(), annot = True, cmap = 'viridis', center = 0, vmin = -1, vmax = 1)
plt.title('Correlation of Closing Price')
plt.tight_layout()
plt.show()

# 5. For each expected return value, how much risk we incur in a particular stock?
area = np.pi*40

plt.figure(figsize = (20,10))
plt.scatter(daily_return.mean(), daily_return.std(), s = area)
plt.xlabel('Expected Return', fontsize = 25)
plt.ylabel('Risk', fontsize = 25)


for label, x, y in zip(daily_return.columns, daily_return.mean(), daily_return.std()):
     plt.annotate(label, xy=(x, y), xytext=(50, 50), textcoords='offset points', ha='right', va='bottom', 
                 arrowprops=dict(arrowstyle='-', color='blue', connectionstyle='arc3,rad=-0.3'))

plt.xticks(rotation = 45)

image_path = '/Users/huuthinle/Downloads/Risk-Expected Return.png'
plt.savefig(image_path)
