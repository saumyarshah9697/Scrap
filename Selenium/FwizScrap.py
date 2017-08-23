import selenium
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
fr=open("FWiz.txt","w")
fr.write("Player,Club,Pos,Rating,Potential,Growth,Age,Contract,Skill Moves,Weak Foot,WorkRate Att.,WorkRate Def.,Foot\n")

def scrap_site():
#     dr=webdriver.Chrome("G:\\Workspace\\IV Processing\\chromedriver.exe")
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    dr = webdriver.Chrome("G:\\Workspace\\IV Processing\\chromedriver.exe",chrome_options=chromeOptions)
    
    
    dr.get("http://www.futwiz.com/en/fifa17/career-mode/players")
    dr.find_element_by_xpath("//*[@id=\"siteContainer\"]/div[3]/form/div[1]/div[1]/fieldset/div[1]/div[2]/div/div/select[1]/option[84]").click()
    el=dr.find_element_by_xpath("//*[@id=\"siteContainer\"]/div[3]/form/input[3]")
    el.send_keys(selenium.webdriver.common.keys.Keys.SPACE)
#     dr.implicitly_wait(10)
#     srt=dr.find_element_by_xpath("//*[@id=\"results\"]/thead/tr/th[3]/a").click()
#     el.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
    while True:
        tab=dr.find_element_by_id("results")
        el=dr.find_element_by_class_name("form-actions").find_element_by_class_name("pull-right").find_element_by_class_name("btn")
        x=scrap_table(tab)
#         el.click()
        el.send_keys(selenium.webdriver.common.keys.Keys.SPACE)
        el.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
        if(not x):
            break

def scrap_table(tab):
    try:
        rows=tab.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
        for x in rows:
            scrap_row(x)
        return True
    except Exception as e:
        print(e)    
        return False
def scrap_row(tr):
    x=tr.find_elements_by_tag_name("td")
    A=x[0].text.split("\n")
    Name=A[0]
    if len(A)==2:
        Club=A[1]
    else:
        Club="None"
    Position=x[1].text
    Rating=x[2].text
    Potential=x[3].text
    Growth=x[4].text
    Age=x[5].text
    Contract=x[6].text
    Skill=x[7].text
    Weak=x[8].text
    Foot=x[10].text
    
    a=x[9].find_elements_by_tag_name("img")
    Att=str(a[0].get_attribute("src")).split("/")[-1].split(".")[0].split("-")[1]
    Def=str(a[1].get_attribute("src")).split("/")[-1].split(".")[0].split("-")[1]    
    
    fr.write(Name+","+Club+","+Position+","+Rating+","+Potential+","+Growth+","+Age+","+Contract+","+Skill+","+Weak+","+Att+","+Def+","+Foot)
    fr.write("\n")

scrap_site()
fr.close()
