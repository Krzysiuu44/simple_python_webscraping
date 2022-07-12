import csv

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

PATH = "../pythonProject17/webdriverFile/msedgedriver.exe"
PATH2 = "webdriverFile/chromedriver.exe"

driver = webdriver.Chrome(PATH2)
#driver = webdriver.Edge(PATH)

link = "https://sklepy.bikeworld.pl/sklepy/rowerowy?strona="

tabela = []
fields = ["nazwa", "adres", "nip", "telefon", "mail"]

with open('plik.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    #csvwriter.writerow(fields)



    def przejedz_strone(numer):
        obecna_strona = link + str(numer)
        driver.get(obecna_strona)
        tbody = driver.find_element(by=By.CSS_SELECTOR, value='.item-list-table tbody')
        tbody_rows = tbody.find_elements(by=By.CSS_SELECTOR, value='tr .item-name a')
        for tbody_row in tbody_rows:
            temp = tbody_row.get_attribute('href')
            if temp == "https://sklepy.bikeworld.pl/sklep/rowerowy/ul_barniewicka_13a/1939/kolomanski_rowery_1":
                break
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(temp)
            time.sleep(0.4)
            nazwa = driver.find_element(by=By.CSS_SELECTOR, value='.profile-full-name h1 span').text
            adress = ""
            for singleSpan in driver.find_elements(by=By.CSS_SELECTOR, value='.about .col-1 h3 span'):
                adress = adress + " " + singleSpan.text
            try:
                nowy = driver.find_element(by=By.CSS_SELECTOR, value='.about .col-1 p').text
                nip = ''.join(char for char in nowy if char.isdigit())
                nip = nip[:10]
                if len(nip) < 9:
                    nip = 0
            except NoSuchElementException:
                nip = "0"
            try:
                tel = "" + driver.find_element(by=By.CSS_SELECTOR, value='.about .col-1 p span').text
                telefon = ''.join(char for char in tel if char.isdigit())
                if telefon[:2] == "48":
                    telefon = telefon[2:11]
                else:
                    telefon = telefon[:9]
            except NoSuchElementException:
                telefon = "0"
            try:
                mail = driver.find_element(by=By.CSS_SELECTOR, value='.about .col-1 p a').text
            except NoSuchElementException:
                mail = "0"
            tab = [nazwa, adress, nip, telefon, mail]
            csvwriter.writerow(tab)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    for numer in range(54, 55):
        przejedz_strone(numer)

