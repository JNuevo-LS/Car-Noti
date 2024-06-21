from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from smtplib import SMTP_SSL as SMTP #Secure Protocol
from email.mime.text import MIMEText

#TODO Implement firefox profile usage

driver = webdriver.Firefox(options=None)

#Facebook Loop
driver.get("https://www.facebook.com/marketplace/category/vehicles")

#TODO Create selection of price, year range, make, model, etc

#TODO Create iteration script

def checkKBB(): #Check the Kelley Blue Book pricing of a specific car
    pass

