from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
import pandas as pd
from datetime import datetime

driver = webdriver.Chrome(options=options)


base_url = "https://www.watchfinder.co.uk/new-arrivals?pageno={}"
total_pages = 72
product_urls = []

for i in range(1, total_pages+1):
    url = base_url.format(i)
    driver.get(url)
    for link in driver.find_elements(By.TAG_NAME, "a"):
        href = link.get_attribute("href")
        if href and "/item/" in href:
            product_urls.append(href)

items = []
for url in product_urls:
    driver.get(url)
    item_id = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/h1/span[3]')
    name = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/h1/span[2]')
    brand = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/h1/span[1]')
    price = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/span[1]')
    model = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/h1/span[2]')
    model_number = driver.find_element(By.XPATH, '//*[@id="content"]/section[3]/div[1]/ul')
    year = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[3]/td[2]')
    description = driver.find_element(By.XPATH, '//*[@id="description-content"]/p')
    box = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[1]/td[2]')
    paper = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[2]/td[2]')
    case_size = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[6]/td[2]')
    case_material = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[7]/td[2]')
    movements = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[8]/td[2]')
    bracelet_material = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[9]/td[2]')
    water_resistance = driver.find_element(By.XPATH, '//*[@id="specification-content"]/table/tbody/tr[11]/td[2]')
    items.append({
        'ItemID': item_id.text,
        'Name': name.text,
        'Brand': brand.text,
        'Price': price.text,
        'FinalPrice': None,
        'EstimatedRetailPrice': None,
        'Currency': 'pounds',
        'FetchDate': datetime.today().strftime('%Y-%m-%d'),
        'URL': url,
        'Model': model.text,
        'ModelNumber': model_number.text,
        'Year': year.text,
        'Description': description.text,
        'Box': box.text,
        'Paper': paper.text,
        'CaseSize': case_size.text,
        'CaseMaterial': case_material.text,
        'Movements': movements.text,
        'BraceletMaterial': bracelet_material.text,
        'dail type':None,
        'brand colur':None,
        'water_resistance':water_resistance.text
    })
df = pd.DataFrame(items)
print(df)           
df.to_excel("/home/farjana/WATCHFINDER.xlsx", index = False)
driver.quit()
