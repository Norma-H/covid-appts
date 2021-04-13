#!/usr/bin/env python3

from selenium import webdriver
from twilio.rest import Client

browser = webdriver.Chrome()
browser.implicitly_wait(10)

def get_website(url, title_word):
    browser.get(url)
    assert title_word in browser.title

def by_class_name(class_name):
    elements = browser.find_elements_by_class_name(class_name)
    all_texts = [e.text for e in elements]
    return all_texts

def phrase_by_iframe(class_name):
    elem = browser.find_element_by_id('openSchedulingFrame')
    browser.switch_to.frame(elem)
    elements = browser.find_elements_by_class_name(class_name)
    for one_elem in elements:
        text = browser.find_element_by_class_name('nodata')
        inner_html = text.get_attribute('innerHTML')
        if 'no available appointments.' in inner_html:
            return 'No'
    else:
        return 'Yes'

def check_for_phrase(all_texts, phrase):
    for one_el in all_texts:
        if phrase in one_el:
            return 'No'
    else:
        return 'Yes'


websites = {'https://apps6.health.ny.gov/doh2/applinks/cdmspr/2/counties?OpID=BB8F752136310A04E0530A6C7C16CBAF':
                ['Welcome to CDMS', 'center', 'No Appointments Available'],
    'https://healow.com/apps/jsp/webview/openaccess/widgets/uc/ucFacility.jsp?apu_id=305742&facility_id=7':
                ['healow', 'fnt14-light-grey', "No appointment availabilities."],
             'https://www.hackensackmeridianhealth.org/covid19/covid-19-vaccine-registration/':
                 ['Hackensack Meridian Health', 'errormessage', 'no available appointments.']}
alert = []
for url, attributes in websites.items():
    title_word, class_name, phrase = attributes
    get_website(url, title_word)
    if 'Hackensack' in title_word:
        status = phrase_by_iframe(class_name)
    else:
        all_texts = by_class_name(class_name)
        status = check_for_phrase(all_texts, phrase)
    if status == 'Yes':
        alert.append(url)

browser.quit()
if len(alert) > 0:
    # print('Alert!')
    account_sid = 'AC57e3934faeada9eae5b2808218509ea2'
    auth_token = '82116d1a6bc21a751f520bb6a04fd7ff'
    client = Client(account_sid, auth_token)
    nl = '\n\n'
    message = client.messages.create(body=f"Available on the following sites:\n{nl.join(alert)}",
                                     from_='+12182033819',
                                     to='+19177506960')
    print(message.sid)