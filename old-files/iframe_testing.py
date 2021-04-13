from selenium import webdriver

browser = webdriver.Chrome()
website = 'https://www.hackensackmeridianhealth.org/covid19/covid-19-vaccine-registration/'
browser.implicitly_wait(10)
browser.get(website)
assert 'COVID-19' in browser.title

#try:
elem = browser.find_element_by_id('openSchedulingFrame')
browser.switch_to.frame(elem)
elements = browser.find_elements_by_class_name('errormessage')

status = 'Yes'
for one_elem in elements:
    # print(f'within {one_elem}')
    text = browser.find_element_by_class_name('nodata')
    inner_html = text.get_attribute('innerHTML')
    # print(inner_html)
    if 'no available appointments.' in inner_html:
        status = 'No'

# try except the not loading error on website
if status == 'Yes':
    print('Alert!')
    #browser.quit()
else:
    print('out of luck')
    #browser.quit()