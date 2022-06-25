import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from Signup import Basic_Unique_Signup_Process
from Login import Basic_Login_Process
from Universal_Dependencies import variableInputs as VI
from PIL import Image
from Screenshot import Screenshot_Clipping
from pathlib import Path
import pyautogui



class StartTestMaster:
    thisDir = Path(os.getcwd())
    ser = Service(str(thisDir.parent) + "\chromedriver.exe")
    op = webdriver.ChromeOptions()
    ss = Screenshot_Clipping.Screenshot()

    # print(str(thisDir.parent) + "\chromedriver.exe")
    try:

        op.add_argument("--start-maximized")

    except Exception as e:
        print(e)
        print("Chrome-path: " + str(ser))
        exit()
    test_driver = webdriver.Chrome(service=ser,
                                   options=op)  # must add the chromedriver.exe to machine's PATH beforehand
    test_driver.get(VI.variableInputs.websiteURL)  # This navigates to the demoblaze site.

    bsp = Basic_Unique_Signup_Process.Signup()
    bsp.click_signup_button(test_driver)
    bsp.input_signup_username(test_driver, VI.variableInputs.unique_username)
    bsp.input_signup_password(test_driver, VI.variableInputs.unique_password)
    bsp.click_signup_modal_signup_button(test_driver)

    time.sleep(2)

    # the commented out sections of screenshot code below cannot create a screenshot without handling the Alert first
    # test_driver.save_screenshot('./Test_Screenshots/Sign_Up_Result.png')
    # ss.full_Screenshot(test_driver, save_path='./Test_Screenshots', image_name='Sign_Up_Result')

    pyautogui.screenshot().save(str(thisDir.parent)+r'\Test_Screenshots\Sign_Up_Result.png')# Does not work with headless
    Alert(test_driver).accept()
    time.sleep(5)
    test_driver.refresh() # refreshes the webpage

    blp = Basic_Login_Process.Login()
    blp.click_login_button(test_driver)
    blp.input_login_username(test_driver, VI.variableInputs.unique_username)
    blp.input_login_password(test_driver, VI.variableInputs.unique_password)
    blp.click_login_modal_login_button(test_driver)

    time.sleep(5)

    # test_driver.save_screenshot('./Test_Screenshots/Log_In_Result.png')
    # ss.full_Screenshot(test_driver, save_path='./Test_Screenshots', image_name='Log_In_Result')
    pyautogui.screenshot().save(str(thisDir.parent)+r'\Test_Screenshots\Log_In_Result.png')# Does not work with headless
    time.sleep(5)

    test_driver.close()
