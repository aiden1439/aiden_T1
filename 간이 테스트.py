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

 ##카카오톡 실행
#    def test(self) -> None:
 #       self.driver.find_element(AppiumBy.XPATH, '//*[@text="카카오톡"]').click()


##사이드메뉴 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="메뉴 더보기"]'))).click()

##게시판 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="게시판"]'))).click()

##글쓰기 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="글쓰기"]'))).click()

##사진 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="사진"]'))).click()


#첨부 파일 이용 기간 안내 팝업
        try:
            # "검색 결과가 없습니다." 텍스트가 있는 요소 찾기
            result_text = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.kakao.talk:id/txt_title"]')
            s_button = WebDriverWait(self.driver, 50).until(
                EC.element_to_be_clickable((
                    AppiumBy.XPATH,'//android.widget.Button[@text="다시보지않음"]')))
            s_button.click()
        except NoSuchElementException:
            # 텍스트가 안 뜨면 넘어감
            print("검색 결과 있음 → X 버튼 클릭 생략")