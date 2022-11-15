import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys
sys.stdout.reconfigure(encoding='utf-8')

def dr(dollars_list):
    dollars = [float(str(dollars_list[i-1])[4: -5]) for i in range(len(dollars_list)-1, 3, -3)]
    dates = [str(dollars_list[i-2])[6: -5] for i in range(len(dollars_list)-1, 3, -3)]
    return dates, dollars

if __name__ == "__main__":
    page = requests.get('https://mfd.ru/currency/?currency=USD')
    soup = BeautifulSoup(page.text, 'html.parser')
    dollars = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
    dollars_list = dollars.find_all('td')
    print(dollars_list)
    dates, dollars = dr(dollars_list)
    print(dr(dollars_list))
    x, ax = plt.subplots()
    ax.xaxis.set_major_locator(MaxNLocator(8))
    ax.grid(True)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Dollars', fontsize=12)
    ax.plot(dates, dollars)
    plt.show()