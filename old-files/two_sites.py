#!/usr/bin/env python3

from selenium import webdriver
from twilio.rest import Client

def check_website_changes(phrase):
    elem = browser.find_elements_by_class_name(classname)
    all_elements = [e.text for e in elem]
    if phrase in all_elements:
        browser.quit()
        return "Sorry - out of luck"
    else:
        return "Alert!"

def check_website_changes_iframe():
    elem = browser.find_element_by_id('openSchedulingFrame')
    browser.switch_to.frame(elem)
    elements = browser.find_elements_by_class_name('errormessage')
    status = 'Alert!'
    for one_elem in elements:
        # print(f'within {one_elem}')
        text = browser.find_element_by_class_name('nodata')
        inner_html = text.get_attribute('innerHTML')
        # print(inner_html)
        if 'no available appointments.' in inner_html:
            status = 'Sorry - out of luck'
            browser.quit()
    return status


browser = webdriver.Chrome()
browser.implicitly_wait(10)
websites = {'https://www.centersurgentcare.net/vaccination':
                ['Centers', 'mb-3', 'IMPORTANT HOLIDAY NOTICE'],
            #'https://healow.com/apps/jsp/webview/openaccess/widgets/uc/ucFacility.jsp?apu_id=305742&facility_id=7':
               # ['healow', 'fnt14-light-grey', 'No appointment availabilities.'],
            'https://www.hackensackmeridianhealth.org/covid19/covid-19-vaccine-registration/':
                ['Hackensack Meridian Health', 'errormessage', "no available appointments."]}

available = []
for url, attributes in websites.items():
    word, classname, phrase = attributes
    browser.get(url)
    assert word in browser.title
    if word == 'Hackensack Meridian Health':
        status = check_website_changes_iframe()
    else:
        status = check_website_changes(phrase)
    if status == "Sorry - out of luck": # when ready to run program for real... change to "Alert!"
        available.append(word)

# account_sid = 'AC57e3934faeada9eae5b2808218509ea2'
# auth_token = '82116d1a6bc21a751f520bb6a04fd7ff'
# client = Client(account_sid, auth_token)
nl = '\n'
print(f"(not) Available on the following sites:\n{nl.join(available)}")
# message = client.messages.create(body=f"(not) Available on the following sites:\n{nl.join(available)}",
                                 # from_='+12182033819',
                                 # to='+19177506960')
# print(message.sid)