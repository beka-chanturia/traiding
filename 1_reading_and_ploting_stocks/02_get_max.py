import pandas as pd

def get_max_close(symbol):
    df = pd.read_csv(f'data/{symbol}.csv')
    return df['Close'].max()

def main():
    print('Max close\n')
    print('-' * 10)
    for symbol in ['AAPL' , 'GLD' , 'IBM' , 'NFLX' , 'SPY']:
        print(symbol + ' : ' , get_max_close(symbol))

if __name__ == '__main__':
    main()
