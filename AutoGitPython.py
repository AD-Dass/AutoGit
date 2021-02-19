
#import math
#import numpy
#import multiprocessing
#import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

fill=sys.argv[1]

def main():
    project_name=fill
    driver = webdriver.Chrome()
    print(fill)
    driver.get("https://www.github.com/login")
    element = driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[2]") #input for username
    element.send_keys("araan@hotmail.co.uk")
    element = driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/input[3]") #input for password
    element.send_keys("")
    element.submit()
    element = driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a") # click to make new_repository
    element.click()
    element = driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input") #Enters new respository name
    element.send_keys(project_name) #lets make this a variable input determined by the intended name of the project
    element = driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[2]/label/input") #makes the project private
    element.click() 
    element =driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]") #makes the read.me file 
    element.click()
    element.submit()
    return "git@github.com:AD-Dass/"+project_name+".git"
if __name__=='__main__':
    main()
else:
    print("There is an error")
