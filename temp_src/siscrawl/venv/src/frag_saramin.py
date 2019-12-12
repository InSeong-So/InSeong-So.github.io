import requests
import math
import re
import openpyxl
import pandas
from datetime import datetime
from bs4 import BeautifulSoup

def saramin_crawler(url):
    print(datetime.now())
    # saramin_result = requests.get("http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2")
    saramin_result = requests.get(url)
    saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")

    total_page_count=saramin_soup.find('span', class_="total_count").get_text()
    numbers=re.findall("\d+",str(total_page_count))

    temp=""
    for numb in numbers:
        temp=temp + str(numb)

    page_count_maximum= math.ceil((int(temp) / 50))
    print("> 총 페이지 : ", page_count_maximum)

    print("> 전체 데이터 병합 시작!")
    whole_source=""
    for page_number in range(1, page_count_maximum):
        URL = 'http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2&page=' + str(page_number)
        response = requests.get(URL)
        whole_source = whole_source + response.text
        print("- ", page_number, " 페이지 종료")
    print("> 병합 완료!")

    print("> html 파싱 시작!")
    soup = BeautifulSoup(whole_source, "html.parser")
    print("> 파싱 종료!")

    all_data = soup.select(".recruiting_list > tbody > tr")

    temp_list = []
    count = 0
    print("=================================크롤링 시작!=================================")
    for detail_data in all_data:
        find_company_nm = detail_data.find("td", {'class':'company_nm'}).find("a", {'class':'str_tit'}).text
        find_title = detail_data.find("td", {'class':'notification_info'}).find("div").find("a")['title']
        find_recruit_condition = detail_data.find("td", {'class': 'recruit_condition'}).text
        find_company_info = detail_data.find("td", {'class': 'company_info'}).text
        find_support_info = detail_data.find("td", {'class': 'support_info'}).text
        temp_list.append([find_company_nm, find_title, find_recruit_condition, find_company_info, find_support_info])
        count = count + 1
        print(count, " 번째 완료, 회사 명 : ", find_company_nm)

    print("=================================크롤링 종료!=================================")

    data = pandas.DataFrame(temp_list)
    data.columns = ['기업명', '제목', '지원자격', '근무조건', '마감일-등록일']
    data.to_csv('saramin_crawling.csv')