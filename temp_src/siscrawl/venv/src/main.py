import pymysql
from frag_saramin import saramin_crawler

# saramin_crawler("http://www.saramin.co.kr/zf_user/jobs/list/domestic?loc_mcd=101000%2C102000&cat_cd=404%2C407%2C408%2C402%2C409%2C416%2C417%2C406&search_optional_item=n&search_done=y&panel_count=y&isAjaxRequest=0&page_count=50&sort=RL&type=domestic&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2")

db = pymysql.connect(host='101.235.203.94', port=3105, user='sis_user', passwd='sis_user1!', db='SIS_EMPLOYMENT', charset='utf8', autocommit=True, cursorclass=pymysql.cursors.DictCursor)
try:
    cursor = db.cursor()
    sql = "SELECT * FROM company_master ORDER BY SEQ_NO;"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

finally:
    db.close()