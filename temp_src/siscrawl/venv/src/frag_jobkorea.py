import requests
import math
import re
import openpyxl
import pandas
import os

from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

jobkorea_result = requests.get("http://www.jobkorea.co.kr/recruit/joblist?menucode=local&local=I000")
jobkorea_soup = BeautifulSoup(jobkorea_result.text, "html.parser")

total_count=jobkorea_soup.find('em')
print(total_count.text)
# numbers=re.findall("\d+",str(total_count))
# temp=""
# for numb in numbers:
#     temp=temp + str(numb)
# page_count_maximum= math.ceil((int(temp) / 50))

# for page_number in range(1, page_count_maximum):
#     URL = 'http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2&page=' + str(page_number)
#     response = requests.get(URL)
#     whole_source = whole_source + response.text
URL = 'http://www.jobkorea.co.kr/recruit/joblist?menucode=local&local=I000'
response = requests.get(URL)
whole_source = response.text

soup = BeautifulSoup(whole_source, "html.parser")

all_data = soup.select("div.tplList > table")

# for title in all_data:
#     print(title)