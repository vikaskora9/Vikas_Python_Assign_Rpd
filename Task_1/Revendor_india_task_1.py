# Importing necessary module
from selenium import webdriver
from selenium.webdriver.edge.service import Service
driver = webdriver.Edge('C:/Users/vikas/Desktop/TANN_MANN/edgedriver_win64/msedgedriver')  # creating webdriver object
driver.get('https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener')  # getting  url of required page
driver.implicitly_wait(20)
driver.find_element_by_id('accept_cookie').click()  # clicking accept cookie button
link = driver.find_element_by_id('screenerContent')  # getting to iframe
driver.switch_to_frame(link)  # switching to iframe
driver.find_element_by_id('my-screen-tab').click()  # clicking myscreen button
driver.find_element_by_xpath('//*[@id="username"]').send_keys('laboc57506@ampswipe.com')  # filling username
driver.find_element_by_xpath('//*[@id="password"]').send_keys('msJ$eb8EJu72@Bj')  # filling password
driver.find_element_by_xpath('//*[@id="login_form"]/button').click()  # clicking signin button
driver.find_element_by_xpath('//*[@id="btn_run_162817"]').click()  # clicking run button
driver.find_element_by_xpath('//*[@id="screener_table_wrapper"]/div[1]/a[1]').click()# clicking csv button


