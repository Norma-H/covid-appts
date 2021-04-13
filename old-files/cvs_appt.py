#!/usr/bin/env python3

from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.cvs.com/immunizations/covid-19-vaccine?icid=coronavirus-lp-nav-vaccine')
assert 'COVID-19' in browser.title

elem = browser.find_elements_by_id('vaccineinfo-NJ')
texts = [e.text for e in elem]

for one_el in texts:
    print(one_el)
    if 'all appointments in New Jersey are booked.' in one_el:
        print('found')

browser.quit()