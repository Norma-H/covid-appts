#!/usr/bin/env python3

from selenium import webdriver
from twilio.rest import Client

class Website(object):
    def __init__(self, browser, url, classname):
        self.browser = browser
        self.url = url
        self.classname = classname

    def set_up_browser(self, url, key):
        norma = 10
        try:
            self.browser.get(url)
            assert key in self.browser.title
        except ConnectionRefusedError as e:
            print(f'{e}: Refused connection')

    def check_website_changes(self, phrase):
        self.browser.implicitly_wait(10)
        elem = self.browser.find_elements_by_class_name(self.classname)
        all_elements = [e.text for e in elem]
        if phrase in all_elements:
            self.browser.quit()
            return "Sorry - out of luck"
        else:
            return "Alert!"

    def check_website_changes_iframe(self, phrase):
        self.browser.implicitly_wait(10)
        elem = self.browser.find_elements_by_class_name(self.classname)
        all_elements = [e.text for e in elem]
        if phrase in all_elements:
            self.browser.quit()
            return "Sorry - out of luck"
        else:
            return "Alert!"


browser = webdriver.Chrome()

websites = {'https://healow.com/apps/jsp/webview/openaccess/widgets/uc/ucFacility.jsp?apu_id=305742&facility_id=7':
                ['healow', 'fnt14-light-grey', 'No appointment availabilities.'],
            'https://www.hackensackmeridianhealth.org/covid19/covid-19-vaccine-registration/':
                ['Hackensack Meridian Health', 'errormessage', "no available appointments."]}

available = []
for url, attributes in websites.items():
    word, classname, phrase= attributes
    site = Website(browser, url, classname)
    site.set_up_browser(url, word)
    status = site.check_website_changes(phrase)
    if status == "Sorry - out of luck":
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