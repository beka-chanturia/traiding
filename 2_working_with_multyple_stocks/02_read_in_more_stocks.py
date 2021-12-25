import pandas as pd


def main():
    start_date = '2021-01-22'
    end_date = '2021-01-26'
    dates = pd.date_range(start=start_date , end=end_date)
    df1 = pd.DataFrame(index=dates)
    dfSPY = pd.read_csv('data/SPY.csv' ,
                         index_col= 'Date',
                         parse_dates=True,
                         usecols=['Date' , 'Adj Close'])

    dfSPY = dfSPY.rename(columns={'Adj Close' : 'SPY'})
    df1 = df1.join(dfSPY , how='inner').dropna()

    symbols = ['AAPL' , 'GLD' , 'IBM' , 'NFLX']
    for symbol in symbols:
        df_temp = pd.read_csv(
            f'data/{symbol}.csv',
            index_col='Date',
            parse_dates=True,
            usecols=['Date' , 'Adj Close']
        )
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)

    print(df1)


if __name__ == '__main__':
    main()
