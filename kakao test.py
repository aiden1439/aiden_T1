import unittest

import driver
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
    def test(self, count=None) -> None:
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="카카오톡"]').click()


##친구탭 이동
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/iv_tab_icon"])[1]'))).click()
##검색 이동
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.Button[@content-desc="검색 업데이트 됨"])'))).click()
##없는 이름 검색
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.view.View[@resource-id="__root__"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText)'))).click()

        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH,'(//android.view.View[@resource-id="__root__"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText)'))).send_keys("없는 이름 검색")
        sleep(3)

        try:
            # "검색 결과가 없습니다." 텍스트가 있는 요소 찾기
            result_text = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="검색 결과가 없습니다."]')

            # 텍스트가 실제로 일치하는지 확인
            if result_text.text == "검색 결과가 없습니다.":
              #  print("검색 결과 없음 → X 버튼 클릭 시도")

                # X 버튼 기다린 후 클릭
                x_button = WebDriverWait(self.driver, 50).until(
                    EC.element_to_be_clickable((
                        AppiumBy.XPATH,
                        '//android.view.View[@resource-id="__root__"]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.widget.Button[2]')))
                x_button.click()
            else:
                print("검색 결과가 있음")
        except NoSuchElementException:
        # 텍스트가 안 뜨면 넘어감
         print("검색 결과 있음 → X 버튼 클릭 생략")

##존재하는 이름 검색
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.view.View[@resource-id="__root__"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText)'))).click()

        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH,'(//android.view.View[@resource-id="__root__"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.widget.EditText)'))).send_keys("에이든")
        sleep(3)
##스와이프 후 채팅방 탭 이동
        for _ in range(5):
            try:
                chat_tab = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="채팅방"]')
                chat_tab.click()
                break
            except NoSuchElementException:
                # 오른쪽으로 스와이프 (왼→오)
                self.driver.swipe(start_x=200, start_y=1000, end_x=800, end_y=1000, duration=500)

##프로필 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[contains(@text, "에이든2")]'))).click()

##입력 창 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//*[@text="메시지 입력"]'))).click()

##안녕하세요 입력 후 전송
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH,'//*[@text="메시지 입력"]'))).send_keys("안녕하세요")
        sleep(3)

##전송 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="전송"]'))).click()

##이모티콘 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.kakao.talk:id/emoticon_button"]'))).click()

##이모티콘 탭 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="앗추추추 모찌찌찌 이모티콘"]'))).click()


##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[1]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[2]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[3]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[4]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[5]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()


##이모티콘 탭 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="King N Queen, 카드의 제왕 이모티콘"]'))).click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[1]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[2]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[3]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[4]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()

##이모티콘 탭 버튼 선택
        emoticon_btn = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk.emoticon:id/emoticon_icon"])[5]')))
        emoticon_btn.click()
        import time
        (time.sleep(0.1))
        emoticon_btn.click()


##키보드 내림(뒤로가기) 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="뒤로가기"]'))).click()

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

##사진선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[1]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[2]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[3]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[4]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[5]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[6]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[7]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[8]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[9]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[10]'))).click()
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="com.kakao.talk:id/thumbnail"])[11]'))).click()

#확인 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@text="확인"]'))).click()

#완료 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@text="완료"]'))).click()
        sleep(3)

        # upload_progress가 사라질 때까지 최대 100초 대기
        WebDriverWait(self.driver, 100).until(
            EC.invisibility_of_element_located(
                (AppiumBy.XPATH, '//android.widget.ProgressBar[@resource-id="com.kakao.talk.moim:id/upload_progress"]')))

        ##글쓰기 버튼 선택
        WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.Button[@content-desc="글쓰기"]'))).click()

if __name__ == '__main__':
    unittest.main()