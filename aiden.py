
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        self.driver.find_element(by=AppiumBy.XPATH,
                                 value='//androidx.recyclerview.widget.RecyclerView[@resource-id="com.kakao.talk:id/recycler_view"]/android.view.ViewGroup').click()

        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="나와의 채팅"]'))).click()




if __name__ == '__main__':
    unittest.main()