import os
from appium.webdriver import Remote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .custom_logger import LoggerHelper
from appium import webdriver

logger = LoggerHelper.json_logger()

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Screen:
    def __init__(self, driver: Remote, by, locator):
        self.by = by
        self.locator = locator
        self.driver = driver

    def wait_until_element_visible(self):
        try:
            el = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((self.by, self.locator))
            )

            if el:
                print('Element found')
                logger.info("Element {0} Found".format(self.locator))
                return True
            else:
                return False
        except TimeoutException:
            return False

class Context:
    def __init__(self, driver):
        self.driver = driver

    def change_to_webview(self):
        contexts = self.driver.contexts
        current_context = self.driver.current_context

        if 'WEBVIEW' in current_context:
            logger.info('Current Context is Web View')
            pass
        else:
            for cont in contexts:
                if 'WEBVIEW' in cont:
                    print(cont)
                    self.driver.switch_to.context(cont)
                    page_source = self.driver.page_source
                    if '<html><head></head><body></body></html>' not in page_source:
                        logger.info('Current Context is  Web View')
                        break

    def change_to_native(self):
        contexts = self.driver.contexts
        current_context = self.driver.current_context
        if 'NATIVE' in current_context:
            logger.info('Current Context is Native')
            pass
        else:
            for cont in contexts:
                if 'NATIVE' in cont:
                    self.driver.switch_to.context(cont)
                    logger.info('Current Context is Native')
                    break