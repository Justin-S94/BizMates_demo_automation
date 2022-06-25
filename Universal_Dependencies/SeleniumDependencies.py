from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import pickle

# This Python file contains the necessary imports to get ANY selenium function or method to work in the automated tests.
# Absolutely do NOT touch, edit, or manipulate this file unless you know what you are doing.

#To use this, just type in "import SeleniumDependencies as sd" without the quotation marks
#then, prefix all your selenium functions with "sd." without the quotations.
#This is one attempt at