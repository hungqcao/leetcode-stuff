from typing import List, Optional, Sized
import collections
import math
import itertools
import functools
import heapq
from common import ListNode, convertToLinkedList

import requests
import json
import time

class StockInfo:
    def __init__(self, date, open, close) -> None:
        self.date = date
        self.open = open
        self.close = close

def convertDate(date):
    return time.strptime(date, '%d-%B-%Y')

def getAllStocks(firstDate, lastDate):
    stocks = []
    currentPage = 1
    while True:
        request = requests.get(f'https://jsonmock.hackerrank.com/api/stocks?page={currentPage}')
        body = json.loads(request.text)
        if not body['data']:
            break
        ret = parseStockJson(body['data'])
        stocks += ret
        currentPage += 1
    return list(filter(lambda x: x.date >= firstDate and x.date <= lastDate, stocks))

def parseStockJson(data):
    res = []
    for d in data:
        res.append(StockInfo(convertDate(d['date']), d['open'], d['close']))
    return res

def openAndClosePrices(firstDate, lastDate):
    res = getAllStocks(convertDate(firstDate), convertDate(lastDate))
    for s in res:
        dateStr = time.strftime('%d-%B-%Y', s.date)
        print(f'{dateStr} {s.open} {s.close}')
    return

print(openAndClosePrices('1-January-2000', '11-January-2000'))

# sol = Solution()
# print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
# print(sol.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
# print(sol.longestBeautifulSubstring("a"))