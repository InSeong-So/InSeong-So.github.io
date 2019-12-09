from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chromedriver ='/Users/soinseong/Documents/workspace/python/chromedriver'
driver = webdriver.Chrome(chromedriver)

# 크롤링할 사이트 호출
driver.get("https://www.opensalary.com/")

# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
# assert "Python" in driver.title

# <input id="id-search-field" name="q" 검색창 name으로 검색하기
# 태그 name으로 특정한 태그를 찾을 수 있음
elem = driver.find_element_by_name("q")

# input 텍스트 초기화
# elem.clear()

# 키 이벤트 전송가능함
# 태그가 input 태그이므로 입력창에 키이벤트가 전달되면, 입력값이 자동으로 작성됨
elem.send_keys("휴먼컨설팅그룹")

# 태그가 input 태그이므로 엔터 입력시 form action이 진행됨
elem.send_keys(Keys.RETURN)

# Selenium은 웹테스트를 위한 프레임워크로 다음과 같은 방식으로 웹테스트를 자동으로 진행함 (참고)
assert "No results found." not in driver.page_source

company_data = driver.find_element_by_class_name("cmp-discirption")
company_description = driver.find_element_by_class_name("company_info_summary")
company_info = driver.find_elements(By.CLASS_NAME, "infoBox-list")

print(company_data.text)

print("--------------------------------")

print(company_description.text)

print("--------------------------------")

print(str(company_info[1].text))

# print(str(company_info[1].text) + " : " + str(company_info[1].text))
# print(str(company_info[2].text) + " : " + str(company_info[3].text))
# print(str(company_info[4].text) + " : " + str(company_info[5].text))

# 명시적으로 일정시간을 기다릴 수 있음 (10초 기다림)
time.sleep(1)

# 크롬 브라우저 닫기 가능함
driver.quit()