# https://github.com/Rolstenhouse/uf_api 's source code referenced largely

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from notify import Notify
import dialog
import sys

def CheckSeat(information):
    courseCode = information["CourseCode"]

    options = webdriver.ChromeOptions()

    # Set chrome to run without a head
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')

    # Initialize the driver
    driver = webdriver.Chrome()
    driver.chrome_options=options


    # Takes you to One.uf.edu
    driver.get("https://one.uf.edu/")

    # If you're not logged in, it redirects you to a page with login information

    # Promts you to log in 
    driver.find_element_by_css_selector('.md-primary.md-raised.md-ink-ripple.login-button.md-button').click()


    # Fill the login form and submit it
 
    driver.find_element_by_id('username').send_keys(information['UfId'])
    driver.find_element_by_id('password').send_keys(information['UfPass'])
    driver.find_element_by_id('submit').click()

    # View Schedule and go to Fall 2019 Semester


    # Checks if Log in was successful
    try:
        driver.find_element_by_css_selector('.md-primary.md-button.md-ink-ripple').click()
    except:
        print('INVALID LOG IN')
        driver.close()
        dialog.InvalidLogIn()

    driver.get("https://one.uf.edu/myschedule/2198") # 2198 Set for Fall 2019, see readme for instructions on how to change


    # Clicks the Add Course Button/ OR directs to Fall 2019 Registration Search

    #driver.find_element_by_css_selector('.add-course.ng-scope').click()

    driver.get("https://one.uf.edu/soc/registration-search/2198")  # 2198 Set for Fall 2019, see readme for instructions on how to change

    #Maximizes window b/c WHY NOT
    driver.maximize_window()


    # Searches Course Code
    driver.find_element_by_id('courseCode').send_keys(courseCode)
    driver.find_element_by_id('courseCode').send_keys(Keys.ENTER)


    driver.implicitly_wait(10)
    #element = driver.find_element_by_css_selector('.course-code').text #this works!

    foundCourse = False

    prevSeat = 0

    while( not foundCourse):
        try:
            time.sleep(10) #wait time (seconds) before it refreshes the screen. 
            driver.find_element_by_id('courseCode').send_keys(Keys.ENTER)
            element = driver.find_element_by_css_selector('.open-seat-counter.ng-binding.ng-scope').text #this works!
            
            print(element)

            if (prevSeat != element):
                driver.save_screenshot('OpenCourse.png')
                Notify(element, information["Gmail"], information["GmailPass"])
                prevSeat = element
            #foundCourse = True  #uncomment this line if you want code to stop running if at least one seat is found

        except:
            print('No Course Found')

    driver.close()


    #Stuff that works
    #https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2195&last-control-number=100


