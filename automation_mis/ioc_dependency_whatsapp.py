import gspread
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#change currnet directory
os.chdir('C:\\Users\\panka\\github_repo\\Analytics\\automation_mis')

from methods import *

browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')
wait = WebDriverWait(browser, 600)

browser.find_elements_by_css_selector('[title~=Notes]').click()

"""
# the trick to avoid captcha is to wait for user to enter it manually
# and click the submit button, then wait until an element from the
# next page is located i.e. 'global_ro_code' in this case
element = WebDriverWait(browser, 35).until(
    EC.presence_of_element_located((By.ID, 'global_ro_code'))
)

# Get into the sub-menus of the navigation bar
browser.find_element_by_link_text('View Reports').click()
browser.find_element_by_link_text('Sales Reports').click()
browser.find_element_by_link_text('Nozzle Sales Report').click()

# move mouse curser by xoffset and yoffset to unselect the visible menu-bar
webdriver.ActionChains(browser).move_by_offset(10, 10).perform()

browser.implicitly_wait(10)
select = Select(browser.find_element_by_id("SO"))
select.select_by_visible_text("Odisha State Office")
select = Select(browser.find_element_by_id("DO"))
select.select_by_visible_text("Sambalpur DO")
select = Select(browser.find_element_by_id("SA"))
browser.implicitly_wait(10)

# since the values in the dropdown activates after selection of preceding input.( eg
# SA dropdown activates only after Divisional office get selected); hence it is
# prudent to wait untill all the text is present in the box

element = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.ID, 'SA'), 'ALL')
)

# Download the first excel file
browser.find_element_by_id('excelButton').click()

# Check if the first file is downloaded
path_to_file = 'C:/Users/panka/Downloads/Nozzle Sales Report.xlsx'
while not os.path.exists(path_to_file):
    time.sleep(2)

# selecting date using datepicker calendar
datepicker = browser.find_element_by_id('datetimepicker')
# opening the calendar using the datepicker
datepicker.click()
browser.implicitly_wait(10)

# getting today's day
current_day = date.today().day
# selecting all elements with the class 'ui-state-defualt'. this
# element will only appear after the calendar is open through datepicker
# days is a list of selenium specific data structure
days = browser.find_elements_by_css_selector('.day')

# Since there are double occurence of few tail days such as 29, 30, 31
# in the calendar, it is imperative that correct day is choosen while
# selecting the date. It can be inferred that current date will always
# come after day 1, so to locate the current day, one need to traverse
# from day 1 to day2 ....... day 31 and discard old days of previous month

# Now one need to find the index of the day 1 of the current month
for index, val in enumerate(days):
    if val.text == '1':
        day_1_index = index
        break

# Given the index of day 1, we have to first find the index of today
# in the calendar. Thereafter one can navigate to the preceeding days
# using the index of the days list. Following will find the index of
# current date and will store it in anchor variable.

for index, val in enumerate(days):
    if index >= day_1_index:
        if val.text == str(current_day):
            anchor = index
            break

# This will select the day, 4 days prior from the current day.
days[(anchor-4)].click()
browser.implicitly_wait(10)

# selecting second date calendar using datepicker1
# ----------------------------------------
datepicker_2 = browser.find_element_by_id('datetimepicker1')
datepicker_2.click()
browser.implicitly_wait(10)
days = browser.find_elements_by_css_selector('.day')

# This will select the day, 3 days prior from the current day.
days[(anchor-3)].click()
# Download the excel file
browser.find_element_by_id('excelButton').click()
# Check if the second file is downloaded
path_to_file = 'C:/Users/panka/Downloads/Nozzle Sales Report (1).xlsx'
while not os.path.exists(path_to_file):
    time.sleep(2)

"""
gc = gspread.service_account(filename='credential.json')
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')
data = sh.worksheet('data_transfer').get_all_values()

df = pd.DataFrame(data, columns=data[0])
df = df.drop([0])

df = df[df['Dependency'] == "IOCL"]
df = df[['RO Name', 'Reason for non-transfer of data']]
data = df.to_string()

with open('test.txt', 'a') as f:
    f.write(data)
