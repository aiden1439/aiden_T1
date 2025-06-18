import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException




capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    **{
        "appium:settings[enableMultiWindows]": True,
        "adbExecTimeout": 5000000,
        "uiautomator2ServerInstallTimeout": 5000000
    }
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()


    def test(self) -> None:
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="앗추추추 모찌찌찌 이모티콘"]').click()


##이모티콘 탭 버튼 선택
     emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
      (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[1]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()
