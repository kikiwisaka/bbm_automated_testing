import os
import datetime
from time import sleep
import unittest
from appium import webdriver
from helper import screen
from helper import custom_logger

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

logger = custom_logger.LoggerHelper().json_logger()

class TestBBM(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'Generic Test'
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = "com.bbm.ui.activities.MainActivity"
        desired_caps['startActivity'] = "com.bbm.ui.activities.StartupActivity"
        desired_caps['app'] = PATH(
            './app_collection/BBM-eval-300.3.21.24.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_1_send_chat(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_1_send_chat'))
        logger.info("{0}".format('================='))
        sleep(4)
        if screen.Screen(self.driver, 'xpath', '//android.widget.FrameLayout[@content-desc="Contacts"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView').wait_until_element_visible():
            self.driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Contacts"]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView').click()
            sleep(4)

            if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Bot Demo"]').wait_until_element_visible():
                logger.debug('clicking Bot Demo')
                self.driver.find_element('xpath', '//android.widget.TextView[@text="Bot Demo"]').click()
                sleep(2)

                logger.debug('typing menu')
                mess = self.driver.find_element('xpath', '//android.widget.EditText[@text="Message"]')
                mess.click()

                sleep(2)
                typing = self.driver.find_element('xpath', '//android.widget.EditText[@text="Message"]')
                if type:
                    typing.send_keys('menu')

                sleep(3)
                self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Send"]').click()
                sleep(2)

                logger.info('Test case {0} PASSED'.format('test_send_chat'))
                logger.info('---------------------------------------------')
                assert True
            else:
                logger.debug('Bot Demo not found')
        else:
            logger.warning('Test case {0} FAILED'.format('test_send_chat'))
            assert False

    def test_2_open_games(self):
        logger.info("{0}".format('================='))
        logger.info("{0}".format('test_2_open_games'))
        logger.info("{0}".format('================='))
        if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="Discover"]').wait_until_element_visible():
            sleep(3)
            logger.info("{0}".format('Opening Discover'))
            self.driver.find_element('xpath', '//android.widget.TextView[@text="Discover"]').click()
            sleep(5)
            if screen.Screen(self.driver, 'xpath', '//android.widget.TextView[@text="BBM Services"]'):
                self.driver.find_element('xpath', '//android.widget.TextView[@text="Instant Games"]').click()
                sleep(5)
                logger.info("{0}".format('Opening Games'))
                screen.Context(self.driver).change_to_webview()
                logger.info("{0}".format('Landing Games'))
                if screen.Screen(self.driver, "xpath", "//span[contains(.,'Dizzy Weather')]"):
                    logger.info('Landing {0} is success.'.format('Games'))
                    logger.info('Test case {0} PASSED'.format('test_2_open_games'))
                    screen.Context(self.driver).change_to_native()
                    logger.info('---------------------------------------------')
