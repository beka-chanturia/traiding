import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/NFLX.csv')
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.savefig('graphs/NFLX.png')

if __name__ == '__main__':
    main()
