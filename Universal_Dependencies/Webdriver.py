import time
import os
import platform
import Universal_Dependencies.SeleniumDependencies as sd



class webDriver:
    BizMates_Demo_Site = "https://www.demoblaze.com/index.html"
    options = sd.Options()
    driver = None
    chromePath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ##Configure this per machine
    actions = None






    def init_webdriver(self, qa):
        # print(os.getcwd())
        ###The following codeblock automatically CHECKS YOUR SYSTEM OS and uses the appropriate webdriver###

        if str(platform.system()) == "Darwin": #MacOS
            print("OS is MacOS")
            print(str(os.path.dirname(os.getcwd())))
            # self.chromePath = str(os.path.dirname(os.getcwd()))+"/chromedriver78Mac"
            self.chromePath = str(os.getcwd()) + "/chromedriver78Mac"
            # self.chromePath = str(os.path.dirname(os.getcwd()))+ "/chromedriver78Mac"
            # chromePath = str(os.getcwd().parent)+"/chromedriver78Mac"
        elif str(platform.system()) == "Linux":
            print("OS is Linux")
            # self.chromePath = str(os.path.dirname(os.getcwd()))+ "/chromedriver76Linux"
            self.chromePath = str(os.getcwd()) + "/chromedriver76Linux"
            self.options.add_argument("--headless")
            # options.add_argument("--disable-dev-shm-usage")
            self.options.add_argument("--no-sandbox")
            os.environ["DISPLAY"] = ":99"
        elif str(platform.system()) == "Windows":
            print("OS is Windows")
            pass
        else: #MacOS Default
            # self.chromePath = str(os.path.dirname(os.getcwd()))+ "/chromedriver78Mac"
                self.chromePath = str(os.getcwd())+ "/chromedriver78Mac"
        self.driver = sd.webdriver.Chrome(self.chromePath, options=self.options)
        self.driver.set_window_size(1920, 1980)


        if str(platform.system()) == "Darwin": #MacOS
            # self.driver.set_window_size(1920, 1980)
            # self.driver.set_window_position(-1920, -(1080 / 2))
            pass
            # self.driver.set_window_size(1440, 900)
            # self.driver.set_window_position(1441, -(1080 / 2))
            # self.driver.set_window_position(0, 0)
        ###END OS CHECK###


        self.actions = sd.ActionChains(self.driver)
        time.sleep(4)
        # listing6test.runSearchByRegion("sg-bedok", "V2")
        print(type(self.driver))
        print("WEBDRIVER INITIALIZED")
