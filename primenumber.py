from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


website = 'https://hprera.nic.in/PublicDashboard'
#please do update update your chrome driver path
chromedriver_path = "/path/to/your/chrome/driver"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.binary_location = chromedriver_path
driver = webdriver.Chrome(options=options)
driver.get(website)
time.sleep(20)



wait = WebDriverWait(driver, 20)
parent_element = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tab-content')))
first_child = parent_element[1].find_elements(By.XPATH, "./*")
second_child = first_child[0].find_elements(By.XPATH, "./*")
third_child = second_child[0].find_elements(By.XPATH, "./*")

elements = third_child[0].find_elements(By.XPATH, "./*")

def details(number):

    first_element = elements[number].find_element(By.XPATH,"./*")
    second_element = first_element.find_element(By.XPATH,"./*")
    values = second_element.find_elements(By.XPATH,"./*")

    values[2].click()
    time.sleep(10)

    wait = WebDriverWait(driver, 20)
    table = wait.until(EC.presence_of_element_located((By.ID, 'project-menu-html')))

    divs = table.find_elements(By.XPATH,"./*")
    second_div = divs[1].find_elements(By.XPATH,"./*")

    inner_div = second_div[0].find_elements(By.XPATH,"./*")
    second_inner_div = inner_div[0].find_elements(By.XPATH,"./*")

    the_table = second_inner_div[0].find_elements(By.XPATH,"./*")
    table_values = the_table[0].find_elements(By.XPATH,"./*")

    def get_element_text_by_label(label, elements):
        for element in elements:
            labels = element.find_elements(By.XPATH, "./*")
            if labels[0].text == label:
                return labels[1].text
        return "Not found"

    name = get_element_text_by_label("Name", table_values)
    pan_no = get_element_text_by_label("PAN No.", table_values)
    gstin_no = get_element_text_by_label("GSTIN No.", table_values)
    permanent_address = get_element_text_by_label("Permanent Address", table_values)

    print(f"Name: {name}")
    print(f"PAN No: {pan_no}")
    print(f"GSTIN No: {gstin_no}")
    print(f"Permanent Address: {permanent_address}")


    close = driver.find_elements(By.CLASS_NAME,'close')
    close[0].click()


for i in range(1, 7):
	print(details(i)) 



time.sleep(100)
