import requests
from bs4 import BeautifulSoup
import re


def getHtmlText(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def get_stockList(lst, stockURL):
    html = getHtmlText(stockURL, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')  # 找到所有的a标签
    for sc in a:
        try:
            href = sc.attrs['href']  # href字段下的股票代码
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])  # 将代码添加到lst列表中

        except:
            continue


def search_baidu_stock(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + '.html'
        # print(url)  # 得到了百度股票url
        html = getHtmlText(url)
        try:
            if html == "":
                continue
            stockNameList = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})
            stockName = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            # print(stockName)
            # print(stockInfo)
            stockNameList.update({"股票名称": stockName.text.split()[0]})
            # print(stockNameList)
            keyList = stockInfo.find_all('dt')  # dt标签下的信息
            valueList = stockInfo.find_all('dd')  # dd
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                stockNameList[key] = value
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(stockNameList) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
            continue


def main():
    stocklist_url = 'http://quote.eastmoney.com/stocklist.html'
    stockinfo_url = 'http://gupiao.baidu.com/stock/'
    output_file = 'F:/BaiduStock//BaiduStockOutput.txt'
    stocklist = []
    get_stockList(stocklist, stocklist_url)
    search_baidu_stock(stocklist, stockinfo_url, output_file)


main()