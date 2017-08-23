from selenium import webdriver
from tqdm import tqdm

dr=webdriver.Chrome("G:\\Workspace\\IV Processing\\chromedriver.exe")
dr.get("http://www.convertcsv.com/generate-test-data.htm")
fw=open("abc.csv","a")

count=10*20

el=dr.find_element_by_id("txt2")
el.clear()
el.send_keys("first,last,age")

el=dr.find_element_by_id("txtRows")
el.clear()
el.send_keys("100000")

el=dr.find_element_by_id("chkDefaultHeader")
el.click()


for x in tqdm(range(count)):

    el=dr.find_element_by_id("btnRun")
    el.click()

    el=dr.find_element_by_id("txta")
    z=str(el.get_attribute("value"))

    fw.write(z)
