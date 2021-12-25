import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/GLD.csv')
    df['High'].plot()
    plt.savefig('graphs/GLD.png')

if __name__ == '__main__':
    main()
