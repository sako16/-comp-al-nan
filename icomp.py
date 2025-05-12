from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time
#pip install selenium webdriver-manager openpyxl

# Setup headless Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the page
url = "https://icomp.az/bakida-komputerler/icomp-pc/"
driver.get(url)
time.sleep(5)  # Wait for JavaScript to load

# Parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Create Excel file
wb = Workbook()
ws = wb.active
ws.title = "icomp pc"
ws.append(["name","details","value"])

# Scrape products
comp2 = soup.find_all("div", class_="productBriefBlock")
comps = soup.find_all("div", class_="product_brief_price_block")

# Minimum ortaq say qədər dövr
count = min(len(comps), len(comp2))

for i in range(count):

#for comps in comp2:    
    name_tag =comp2[i].find("div", class_="productBriefTitle")
    details_tag =comp2[i].find("div", class_="productBriefDescr")
    value_tag =comps[i].find("div", class_="productBriefPrice")    

    name = name_tag.get_text(strip=True) if name_tag else ""
    details = details_tag.get_text(strip=True) if details_tag else ""  
    value = value_tag.get_text(strip=True) if value_tag else ""
        
    if name and details and value:
     ws.append([name, details, value] )     
wb.save("icomp_products.xlsx")
print("Done: icomp_products.xlsx")