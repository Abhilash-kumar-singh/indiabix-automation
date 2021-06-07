from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome("chromedriver")
driver.get('https://www.indiabix.com/online-test/aptitude-test/1')
driver.find_element_by_xpath('//*[@id="btnStartTest"]').click()
ids=['158','161','183','227','228','290','323','322','394','422','488','514','579','665','716','745','755','754','760','777']
count=1
sleep(3)
answer=[]
'''
img=driver.find_element_by_xpath('//*[@id="tdAnswerIMG_A_158"]/img')
string=img.get_attribute('src')
print(string)
'''
for num in ids:
         for ele in ["A","B","C","D","E"]:
                           img=driver.find_element_by_xpath('//*[@id="tdAnswerIMG_{}_{}"]/img'.format(ele,num))
                           string=img.get_attribute('src').split("/")[-1]
                           if(string=="accept.png"):
                                    print("Question"+str(count)+" : "+ele)
                                    answer.append(ele)
                                    break         
         count=count+1
i=0
height=10
for num in ids:
         driver.find_element_by_xpath('//*[@id="optionAns_{}_{}"]'.format(answer[i],num)).click()
         driver.execute_script("window.scrollTo(0,{})".format(height))
         height=height+10
         i=i+1
driver.find_element_by_xpath('//*[@id="btnSubmitTest"]').click()
Alert(driver).accept()
                  
