# from pyvirtualdisplay import Display
# from selenium import webdriver

# display = Display(visible=0, size=(800, 600))
# display.start()
# driver = webdriver.Chrome()
# driver.get('http://christopher.su')
# print(driver.title)

from getpass import getpass 
from selenium import webdriver 
from time import sleep 
  
usr = input('Enter email: ')  
pwd = getpass('Enter Password:')  
  
driver = webdriver.Chrome() 
driver.get('https://www.facebook.com/') 
print("Opened facebook") 
sleep(1) 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 
  
print ("Done") 
input('Press enter to quit') 
driver.quit() 
print("Finished") 