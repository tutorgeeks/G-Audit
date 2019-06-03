import os
from selenium import webdriver
import time
#chrome_d=os.environ['CHROME_DRIVER']
driver = webdriver.Chrome('var/lib/jenkins/workspace/G-Audit/chromedriver') #Path to ChromeDriver installation
driver.implicitly_wait(5)
print "Trying to login into Google..."
driver.get("https://accounts.google.com")
login_field = driver.find_element_by_name("identifier")
login_field.clear()
user_name = os.environ['GMAIL_USERNAME'] #Enter your username here
login_field.send_keys(user_name)
login_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

password_field = driver.find_element_by_name("password")
password_field.clear()
pass_value = os.environ['GMAIL_PASSWORD'] #Enter your password here
password_field.send_keys(pass_value)
password_field.send_keys(u'\ue007') #unicode for enter key
time.sleep(2)

print "Successfully logged into Google..."
fh=open("list","r")

websites=[]
for each in fh.readlines():
    websites.append(each.strip("\n"))
print "List of websites that will be tested:"+" "+str(websites)
driver.implicitly_wait(5)
print "<------- Checking for Google groups misconfiguration ------->"
for i in websites:
    try:
        driver.get("https://groups.google.com/a/"+i)
        check_group = driver.find_element_by_class_name("bodyElement").text
        if "private" in check_group:
            print "No misconfiguration:"+" "+"https://groups.google.com/a/"+str(i)
        else:
            print "Google groups is Misconfigured"
    except:
        print "Something went wrong:"+" "+"https://groups.google.com/a/"+str(i)

driver.implicitly_wait(5)
print "<------- Checking for Google sites misconfiguration ------->"
for j in websites:
    try:
        driver.get("https://sites.google.com/a/"+j+"/sites/system/app/pages/meta/dashboard/categories")
        if driver.find_element_by_class_name("sites-dashboard-categories-list").is_enabled():
            print "Public Sites List:"+" "+"https://sites.google.com/a/"+str(j)
    except:
        print "Access Denied:"+"https://sites.google.com/a/"+str(j)
driver.close()
fh.close()
