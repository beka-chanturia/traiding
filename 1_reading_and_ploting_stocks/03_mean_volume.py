import pandas as pd

def get_mean_volume(symbol):
    df = pd.read_csv(f'data/{symbol}.csv')
    return df['Volume'].mean()
    

def main():
    print('mean volume')
    print('-' * 10)
    for symbol in ['AAPL' , 'GLD' , 'IBM' , 'NFLX' , 'SPY']:
        print(symbol + ' : ' , get_mean_volume(symbol))

if __name__ == '__main__':
    main()
