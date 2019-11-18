print("importing os + subprocess")
import os
import subprocess
print("importing selenium")
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print("importing time")
import time 
print("importing datetime")
from datetime import datetime
print("code start")

open(r'FXResults.txt','w+').close()
driver = webdriver.Chrome()
driver.get('http://app.portoffelixstowe.co.uk/frmContainerEnquiry.aspx')

def ClearButton():
    driver.find_element_by_id('ContentPlaceHolder1_cmdClear').click()

def SubmitButton():
    driver.find_element_by_id('ContentPlaceHolder1_cmdSubmit').click()

def formatresults(collresults):
    table = driver.find_element_by_css_selector('#ContentPlaceHolder1_divSearchResults > table > tbody')
    for row in table.find_elements_by_tag_name("tr")[:-1]:
        rowlist = row.text.split()
        if rowlist[2] == 'No':
            rowlist[2] = 'NOT RELEASED'
        else:
            rowlist[2] = 'OK'
        if len(rowlist) > 15:
            try:
                result = f'{rowlist[0]}\t{datetime.strftime(datetime.strptime(" ".join(rowlist[-4:]), "%d %b %Y %H:%M"), "%d/%m %H:%M")}\t{rowlist[2]}\n'
            except Exception as e:
                pass
                print(e)
        elif 'Vessel' in rowlist:
            try:
                result = (f'{rowlist[0]}\tVESSEL {datetime.strftime(datetime.strptime(" ".join(rowlist[4:9]), "%d %b %Y %H:%M"), "%d/%m %H:%M")}\t{rowlist[2]}\n')
            except Exception as e:
                pass
                print(e)
            try:
                result = (f'{rowlist[0]}\tVESSEL {datetime.strftime(datetime.strptime(" ".join(rowlist[5:9]), "%d %b %Y %H:%M"), "%d/%m %H:%M")}\t{rowlist[2]}\n')
            except Exception as e:
                pass
                print(e)

        elif len(rowlist) > 2:
            if 'TTY' in rowlist[3]:
                rowlist[3] = 'TRINITY'
            elif 'LNG' in rowlist[3]:
                rowlist[3] = 'BERTH 8&9'
            result = (f'{rowlist[0]}\t{rowlist[3]}\t{rowlist[2]}\n')

        print(result[:-1])
        with open(r'FXResults.txt','a') as ResultsFile:
            ResultsFile.write(result)

def main():
    collresults = []
    CollectionsList = []
    done = False
    while not done:
        error1 = 0
        userinput = input('Cont num: ')
        if userinput.lower() in 'done':
            done = True
        elif len(userinput) != 0:
            try:
                userinput = userinput[:11]
            except Exception as e:
                print(e)
                error1 = 1
            if error1 == 0:
                CollectionsList.append(userinput)
            else:
                print('Error: Invalid input')

    composite_list = [CollectionsList[x:x+20] for x in range(0, len(CollectionsList),20)]
    for i in composite_list:
        complete_success = False
        for p in i:
            if ' FX PENTALVER' in p:
                p.replace(' FX PENTALVER','')
            driver.find_element_by_id('ContentPlaceHolder1_txtCollections').send_keys(f'{p}\n')
        while not complete_success:
            try:
                SubmitButton()
                formatresults(collresults)
                ClearButton()
                complete_success = True
            except Exception as e:
                print(f"#### Error: {e}####\n trying again")
            
            

    driver.close()
    driver.quit()
    os.startfile(r'FXResults.txt')


if __name__ == "__main__":
    main()