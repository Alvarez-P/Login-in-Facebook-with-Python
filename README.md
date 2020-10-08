# Login-in-Facebook-with-Python
Login in Facebook with Python- Selenium
## Install tools
  `sudo apt-get install xvfb`
## Install ChromeDriver
    sudo apt-get install unzip

    wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    chmod +x chromedriver

    sudo mv -f chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    
 ## Install some Python dependencies and Selenium
    pip3 install pyvirtualdisplay selenium getpass
  
  
## To test the correct installation of Selenium and Chrome driver
Run in a python file:
    
    from pyvirtualdisplay import Display
    from selenium import webdriver
    display = Display(visible=0, size=(800, 600))
    display.start()
    driver = webdriver.Chrome()
    driver.get('http://christopher.su')
    print driver.title    
