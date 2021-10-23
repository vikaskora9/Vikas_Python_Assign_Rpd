# importing necessary module
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import re
from datetime import datetime

# creating Webdriver object
driver = webdriver.Edge('C:/Users/vikas/Desktop/TANN_MANN/edgedriver_win64/msedgedriver')

# opening data.csv through which we can change

f = open('data.csv', 'r+')
line = f.readlines()
lst = []
driver.get('https://www.zacks.com/funds/etf/veu/holding')
driver.implicitly_wait(20)
driver.find_element_by_id('accept_cookie').click()  # clicking accept cookie button

for i in line:
    lst.append(re.sub('\n', '', i))
for _ in range(1, len(lst)):
    driver.get('https://www.zacks.com/funds/etf/' + str(lst[_]) + '/holding')
    # creating empty lists to put data in it
    date = []
    Sec_Name = []
    Symbol = []
    shares = []
    weight = []
    weight_change = []
    Detail = dict()
    Detail.clear()

    # for time being used this as there was no other option to get number of pages
    if lst[_] == 'xlu':
        pg_len = 4
    elif lst[_] == 'xle':
        pg_len = 3
    elif lst[_] == 'spy':
        pg_len = 51
    elif lst[_] == 'veu':
        pg_len = 361
    # parsing through all pages present in that ticker link
    for j in range(1, pg_len+1):
        try:
            for u in range(1, 11):
                name = driver.find_element_by_xpath('//*[@id="etf_holding_table_wrapper"]/div[2]/div[3]/div[2]/div/table/tbody/tr[' + str(u) + ']/td')
                sym = driver.find_element_by_xpath('//*[@id="etf_holding_table"]/tbody/tr[' + str(u) + ']/td[2]')
                share = driver.find_element_by_xpath('//*[@id="etf_holding_table"]/tbody/tr[' + str(u) + ']/td[3]')
                weig = driver.find_element_by_xpath('//*[@id="etf_holding_table"]/tbody/tr[' + str(u) + ']/td[4]')
                change = driver.find_element_by_xpath('//*[@id="etf_holding_table"]/tbody/tr[' + str(u) + ']/td[5]')
                date.append(datetime.now().date())
                Sec_Name.append(name.text)
                Symbol.append(sym.text)
                shares.append(share.text)
                weight.append(weig.text)
                weight_change.append(change.text)
        except NoSuchElementException:
            break
        # clicking next button to go on next data
        driver.find_element_by_xpath('//*[@id="etf_holding_table_next"]').click()
    # storing in dictionary so that data can be converted to DataFrame
    Detail = {
        'Date': date,
        'Name': Sec_Name,
        'Symbol': Symbol,
        'Share': shares,
        'Weight': weight,
        'WK Change': weight_change
    }
    df = pd.DataFrame(Detail)
    # creating csv file with name ok ticker name
    df.to_csv(str(lst[_]) + '.csv', mode='w')
# veu = 361 , spy = 51 , xle = 3 , xlu = 4
