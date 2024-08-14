from selenium import webdriver
from selenium.webdriver import ChromeOptions
import time
from datetime import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
#keeps the chrome open the detach mode else the service ends as soon .
username="" #Update IRCTCUSERNAME
passwordVal="" #Update IRCTC PASSWORD
source='kota jn'
destination='ratlam jn'
travel_date='17-03-2020'
opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts) #options=opts
wait = WebDriverWait(driver,10)

#
# f=open("station list","+r")
# content=f.read()
#
#
# source = input("Enter From Station Code:").upper()
#
# x=content.find(source)
# print (x)
# while x==-1:
#     source = input("Enter From Station Code:").upper()
#     x = content.find(source)
#     print (x)
# f.close()

# f=open("station list","+r")
# content=f.read()
# destination = input("Enter To Station Code:").upper()
# y=content.find(destination)
# print (y)
# while y==-1:
#     destination = input("Enter To Station Code:").upper()
#     y = content.find(destination)
#     print(y)
#
# travel_date=input("Enter Travel Date(DD-MM-YYYY):")

driver.get("https://www.irctc.co.in/nget/train-search")
hambrgr=driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[1]/div[3]/a/i")
WebDriverWait(driver, 10)
hambrgr.click()
loginBtn=driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/div[3]/p-sidebar/div/nav/div/label/button")
loginBtn.click()
WebDriverWait(driver,100)
loginname=driver.find_element_by_id("userId")
print(loginname.is_displayed())
# loginname.click()
#WebDriverWait(driver, 100)
loginname.send_keys(str(username))
password=driver.find_element_by_id("pwd")

WebDriverWait(driver, 100)
password.send_keys(str(passwordVal))

#otp_chkbox=driver.find_element_by_id("otpLogin")
#otp_chkbox.click()
catpcha=input("Input Captcha or 'SKP' :")
if(catpcha.upper()!="SKP"):
    captcha_text=driver.find_element_by_xpath("/html/body/app-root/app-home/div[2]/app-login/p-dialog/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/app-nlp-captcha/div/div[2]/div/div[3]/div[1]/input")
    captcha_text.send_keys(str(catpcha))
signin_btn=driver.find_element_by_xpath("/html/body/app-root/app-home/div[2]/app-login/p-dialog/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/button")
signin_btn.click()
driver.implicitly_wait(100)

#enterotp=driver.find_element_by_xpath("//*[@id='loginOTP']")
#enterotp.send_keys(str(input("ënter recieved OTP:")))

#otplogin_btn=driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/button")
#otplogin_btn.click()
time.sleep(5.0)



station_from_txt=driver.find_element_by_xpath("//*[@id='origin']/span/input")
station_from_txt.send_keys(str(source))
time.sleep(2.0)

#station_from_txt.send_keys(Keys.RETURN)
station_from_txt.send_keys(Keys.TAB)
station_from_txt.send_keys(Keys.TAB)



station_to_txt=driver.find_element_by_xpath("//*[@id='destination']/span/input")
station_to_txt.send_keys(str(destination))
time.sleep(2.0)

station_to_txt.send_keys(Keys.RETURN)
station_to_txt.send_keys(Keys.TAB)




travel_date_txt=driver.find_element_by_xpath("/html/body/app-root/app-home/div[2]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[3]/p-calendar/span/input")
print (travel_date)
time.sleep(1.0)
travel_date_txt.send_keys(str(travel_date))
time.sleep(1.0)
travel_date_txt.send_keys(Keys.TAB)


findtrain_btn=driver.find_element_by_xpath("/html/body/app-root/app-home/div[2]/div/app-main-page/div[1]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button")
findtrain_btn.click()

time.sleep(5)
trainlist_startpoint=driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div/div[2]/div[3]/span")
print(trainlist_startpoint.is_displayed())
x=0
trainlist=[]
abc=driver.switch_to_active_element()
abc.send_keys(Keys.TAB)
numoftrains=int(abc.get_attribute("aria-label")[:2])
print(numoftrains)
while x<=numoftrains*5:
    x = x+1
    abc=driver.switch_to_active_element()
    abc.send_keys(Keys.TAB)
    # trainlist.append(//*[@id="T_12951"])
    # // *[ @ id = "T_12401"] / span
    #print(abc)
    try:
        #print(abc.get_attribute("aria-label"))
        if 'Check' in str(abc.get_attribute("aria-label")):
            trainlist.append(abc.get_attribute("aria-label"))
    except AttributeError:
        pass
        #print("\n x-o-x No ID found x-o-x")
    #print (abc)
for x in range(1,len(trainlist),2):
    print('\n'+trainlist[x].replace('Check availability & fare for', str(x)))



trainlist_startpoint=driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div/div[2]/div[3]/span")

abc=trainlist_startpoint.send_keys("")
abc=driver.switch_to_active_element()
abc.send_keys(Keys.TAB)
#numoftrains=int(abc.get_attribute("aria-label")[:2])
print(numoftrains)
availability=[]
while len(availability)!=numoftrains:
    abc=driver.switch_to_active_element()
    abc.send_keys(Keys.TAB)
    # trainlist.append(//*[@id="T_12951"])
    # // *[ @ id = "T_12401"] / span
    #print(abc)
    try:
        #print(abc.get_attribute("aria-label"))
        if 'T_' in str(abc.get_attribute("id")):
            availability.append(str(abc.get_attribute("id")))
            abc.send_keys(Keys.TAB)
            # availability.append(str(abc.get_attribute("id").replace('T_', 'Train#:')))
            #print(availability)
        if 'check-availability' in str(abc.get_attribute("id")):
            pass
            #abc.send_keys(Keys.RETURN)
            #abc.send_keys(Keys.TAB)

    except AttributeError:
        pass
        #print("\n x-o-x No ID found x-o-x")
    #print (abc)

for x in range(len(availability)):
    trainDetail=driver.find_element_by_id(str(availability[x]))
    trainDetail.send_keys("")
    if str(driver.find_elements_by_class_name("t_5").get_attribute("value"))==str(datetime.strptime(travel_date,"%d %b %Y")):
        waitingstatus=driver.find_elements_by_class_name("waitingstatus")
        if 'AVAILABLE-' in str(waitingstatus.get_attribute("value")):
            str(availability[x]).replace('T_', 'Train#:')

    driver.find_elements_by_class_name("waitingstatus")
    print('\n'+availability[x])
    x=x+1


