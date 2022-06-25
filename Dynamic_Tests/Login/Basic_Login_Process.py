from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Universal_Dependencies.xPathDefs import xPathDefs
from Universal_Dependencies.variableInputs import variableInputs


class Login:

    def click_login_button(self, test_driver):

        # test_driver.get(variableInputs.websiteURL)  # This opens the demoblaze site.

        # Click Sign Up button in Header
        try:
            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.presence_of_element_located((By.XPATH, xPathDefs.homepage_login_button)))
            # print("Element located!")
            test_driver.find_element(By.XPATH, xPathDefs.homepage_login_button).click()
        except Exception as e:
            print("Error on clicking the Signup Button")
            print(e)
            exit()
            pass

    def input_login_username(self, test_driver, unique_username):
        # Input username into Username Field in Log In Popup
        try:
            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_modal)))

            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_popup_username_field)))

            test_driver.find_element(By.XPATH, xPathDefs.homepage_login_popup_username_field).send_keys(
                unique_username)

            print("The unique username for this session is: "+unique_username)
        except Exception as e:
            print("Error on inputting in the Username Field")
            print(e)
            exit()
            pass

    def input_login_password(self, test_driver, unique_password):
        # Input password into Password Field in Log In Popup
        try:
            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_modal)))

            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_popup_password_field)))

            test_driver.find_element(By.XPATH, xPathDefs.homepage_login_popup_password_field).send_keys(
                unique_password)

            print("The unique password for this session is: " + unique_password)
        except Exception as e:
            print("Error on inputting in the Password Field")
            print(e)
            exit()
            pass

    def click_login_modal_login_button (self, test_driver):
        # Finish the log in process by clicking the Log in button inside the Log in modal
        try:
            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_modal)))

            WebDriverWait(test_driver, variableInputs.waitDelay).until(
                EC.visibility_of_element_located((By.XPATH, xPathDefs.homepage_login_popup_login_button)))

            test_driver.find_element(By.XPATH, xPathDefs.homepage_login_popup_login_button).click()


        except Exception as e:
            print("Error on inputting in the Password Field")
            print(e)
            exit()
            pass
