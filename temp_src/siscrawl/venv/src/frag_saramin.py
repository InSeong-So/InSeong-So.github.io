import requests
import math
import re
import openpyxl
import pandas
import os

from bs4 import BeautifulSoup

## python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# jobkorea_result = requests.get("https://www.jobplanet.co.kr/job_postings/search?utf8=%E2%9C%93&jp_min_overall=3.0&jp_min_salary=0&jp_min_recommend=70&recruitment_type_ids%5B%5D=1&city_ids%5B%5D=1&city_ids%5B%5D=2&occupation_level2_ids%5B%5D=11604&occupation_level2_ids%5B%5D=11607&occupation_level2_ids%5B%5D=11613&occupation_level2_ids%5B%5D=11614&job_type_ids%5B%5D=3&job_type_ids%5B%5D=1&order_by=score")
saramin_result = requests.get("http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2")
jobkorea_result = requests.get(
    "https://www.jobplanet.co.kr/job_postings/search?utf8=%E2%9C%93&jp_min_overall=3.0&jp_min_salary=0&jp_min_recommend=0&city_ids%5B%5D=1&city_ids%5B%5D=2&occupation_level2_ids%5B%5D=11607&occupation_level2_ids%5B%5D=11604&occupation_level2_ids%5B%5D=11613&occupation_level2_ids%5B%5D=11614&job_type_ids%5B%5D=3&job_type_ids%5B%5D=1&order_by=score")
saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")
jobkorea_soup = BeautifulSoup(jobkorea_result.text, "html.parser")

total_count=saramin_soup.find('span', class_="total_count").get_text()
numbers=re.findall("\d+",str(total_count))
temp=""
for numb in numbers:
    temp=temp + str(numb)
page_count_maximum= math.ceil((int(temp) / 50))

whole_source=""
for page_number in range(1, page_count_maximum):
    URL = 'http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2&page=' + str(page_number)
    response = requests.get(URL)
    whole_source = whole_source + response.text

soup = BeautifulSoup(whole_source, "html.parser")

all_data = soup.select(".recruiting_list > tbody > tr")

#.text
# find_company_nm = soup.select(".recruiting_list > tbody > tr > td.company_nm > a.str_tit")
#['title']
# find_title = soup.select(".recruiting_list > tbody > tr > td.notification_info > div > a")
#.text
# find_recruit_condition = soup.select(".recruiting_list > tbody > tr > td.recruit_condition")
#.text
# find_company_info = soup.select(".recruiting_list > tbody > tr > td.company_info")
#.text
# find_support_info = soup.select(".recruiting_list > tbody > tr > td.support_info")
temp_list = []
for detail_data in all_data:
    find_company_nm = detail_data.find("td", {'class':'company_nm'}).find("a", {'class':'str_tit'}).text
    find_title = detail_data.find("td", {'class':'notification_info'}).find("div").find("a")['title']
    find_recruit_condition = detail_data.find("td", {'class': 'recruit_condition'}).text
    # find_recruit_condition1 = detail_data.find("td", {'class': 'recruit_condition'}).find("p", {'class':'career'}).text
    # find_recruit_condition2 = detail_data.find("td", {'class': 'recruit_condition'}).find("p", {'class':'education'}).text
    find_company_info = detail_data.find("td", {'class': 'company_info'}).text
    find_support_info = detail_data.find("td", {'class': 'support_info'}).text
    # print(find_company_nm, find_title, find_recruit_condition1, find_recruit_condition2, find_company_info, find_support_info)
    temp_list.append([find_company_nm, find_title, find_recruit_condition, find_company_info, find_support_info])

data = pandas.DataFrame(temp_list)
data.columns = ['기업명', '제목', '지원자격', '근무조건', '마감일-등록일']
data.to_csv('saramin_crawling.csv')