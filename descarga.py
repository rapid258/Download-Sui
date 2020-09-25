import os
import time
import datetime
from selenium import webdriver# I need to web scrap in chrome
from selenium.webdriver.support.select import Select # I need to select menu options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint

def navmenu(var,loc):
    driver.implicitly_wait(10)
    if var=="age":
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/select/option[%s]"%(str(loc+1)))
    if var=="site":
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/select/option[%s]"%(str(loc+1)))
    if var=="data":
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[7]/td[2]/select/option[%s]"%(str(loc)))
    if var=="month":
        inputElement = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/select/option[%s]"%(str(loc+1)))
    #element_present = expected_conditions.presence_of_element_located((By.xpath, "/html/body/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/select/option[%s]"%(str(loc+1))))
    #WebDriverWait(driver, 6).until(element_present)
    webtext=inputElement.text
    webdata=inputElement

    return (webtext,webdata)

url="http://reportes.sui.gov.co/fabricaReportes/frameSet.jsp?idreporte=ele_com_096"
sistemaop = os.name
if sistemaop=="posix":
    driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
else:
    driver = webdriver.Chrome('./chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get(url)
time_delay = randint(30,55)
time.sleep(time_delay)
dheader=driver.find_element_by_xpath("//*[@id='header']")
driver.switch_to.frame(dheader)

a=navmenu("age",1)
print (a)
