import requests

from bs4 import BeautifulSoup

search_company = {'q':'휴먼컨설팅그룹', 'c':'휴먼컨설팅그룹'}

with requests.Session() as s:
    first_page = s.get("https://www.opensalary.com")

    html = first_page.text
    soup = BeautifulSoup(html,"html.parser")

    login_req = s.post('https://www.opensalary.com/company/', data=search_company)
    # 어떤 결과가 나올까요?
    print(login_req.text)