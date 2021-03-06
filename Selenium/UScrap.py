from selenium import webdriver

dr=webdriver.Chrome("G:\\Workspace\\IV Processing\\chromedriver.exe")

dr.get("http://yocket.in/universities/top-25")
A=dr.find_elements_by_class_name("col-sm-10")
f=open("CollegeScrapped.csv","w")

f.write("College,State,Rank,Type,Fees,Acceptance\n")
for B in A:
    C=B.find_element_by_class_name("col-sm-9").find_element_by_tag_name("h4")
    Name=C.find_element_by_tag_name("a").text.replace(",","-")
    f.write(Name+",")
    City=C.find_element_by_tag_name("small").text.replace(",","-")
    f.write(City+",")
    Rank=B.find_element_by_class_name("col-sm-3").find_element_by_tag_name("h4").find_element_by_tag_name("span").text.replace(",","::")
    f.write(Rank+",")
    Details=B.find_element_by_class_name("col-sm-12").find_element_by_tag_name("p").find_element_by_tag_name("small").text
    (Type,Fees,Acceptance)=Details.split("\n")
    Type=Type.split(" ")[0]
    Fees=Fees.split(" ")[0].replace(",","")
    Acceptance=Acceptance.split("%")[0]
    if(Type=="Public" and int(Fees.replace("$",""))>=40000):
        Fees="Anomaly Detected"
        
    if(Type=="Private" and int(Fees.replace("$",""))>=60000):
        Fees="Anomaly Detected"
    
    f.write(Type+",")
    f.write(Fees+",")
    f.write(Acceptance+",")
    f.write("\n")
print("Done")