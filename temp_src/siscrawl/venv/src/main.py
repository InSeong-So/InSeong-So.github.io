import requests
from bs4 import BeautifulSoup

jobkorea_result = requests.get("https://www.jobplanet.co.kr/job_postings/search?utf8=%E2%9C%93&jp_min_overall=3.0&jp_min_salary=0&jp_min_recommend=70&recruitment_type_ids%5B%5D=1&city_ids%5B%5D=1&city_ids%5B%5D=2&occupation_level2_ids%5B%5D=11604&occupation_level2_ids%5B%5D=11607&occupation_level2_ids%5B%5D=11613&occupation_level2_ids%5B%5D=11614&job_type_ids%5B%5D=3&job_type_ids%5B%5D=1&order_by=score")
jobkorea_soup = BeautifulSoup(jobkorea_result.text, "html.parser")
jobkorea_div = jobkorea_soup.find('p', class_='company_name')


print(jobkorea_div)