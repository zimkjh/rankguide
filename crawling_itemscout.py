import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def loginAndFilterAtFirst():
    # 로그인
    login_button_can = driver.find_elements(By.CLASS_NAME, "v-btn__content")
    login_button = [x for x in login_button_can if x.text == '로그인/회원가입'][0]
    login_button.click()
    time.sleep(10)

    input_list = driver.find_elements(By.TAG_NAME, "input")
    input_list[0].send_keys("zimkjh@naver.com")

    f = open("config.txt", "r")
    password = f.readline()
    f.close()
    input_list[1].send_keys(password)

    login_submit_can = driver.find_elements(By.CLASS_NAME, "v-btn__content")
    login_submit = [x for x in login_submit_can if "이메일 로그인" in x.text][0]
    login_submit.click()
    time.sleep(10)

    # 필터 선택하기
    brand_delete = driver.find_elements(By.CLASS_NAME, "option")[4]
    brand_delete.click()
    time.sleep(3)

    search_min = driver.find_elements(By.ID, "inputstartundefined")[0]
    search_min.send_keys(1000)
    time.sleep(3)

    items_max = driver.find_elements(By.ID, "inputendundefined")[1]
    items_max.send_keys(100)
    time.sleep(3)

    just_click = driver.find_elements(By.ID, "inputendundefined")[2]
    just_click.click()
    time.sleep(3)


itemscout_url = "https://itemscout.io/category"

driver = webdriver.Firefox()
driver.get(itemscout_url)
time.sleep(5)

# 초기 팝업 제거
cancel_button = driver.find_element(By.CLASS_NAME, "btn-cancel")
cancel_button.click()
time.sleep(3)

# 카테고리 1 우선 선택
category1 = driver.find_element(By.CLASS_NAME, "its-dropdown")
category1.click()
time.sleep(3)

category1_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
category1_list = [x for x in category1_list if x.text != '']

isFirst = True
isCategory1First = True

for idx1 in range(len(category1_list) - 1):
    if idx1 < 9 or idx1 > 11:
        continue

    category1_item = category1_list[idx1]

    if isCategory1First:
        isCategory1First = False
    else:
        category1 = driver.find_element(By.CLASS_NAME, "its-dropdown")
        category1.click()
        time.sleep(3)

        category1_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
        category1_list = [x for x in category1_list if x.text != '']
        category1_item = category1_list[idx1]

    category1_item.click()
    time.sleep(3)

    category2 = driver.find_elements(By.CLASS_NAME, "its-dropdown")[1]
    category2.click()
    time.sleep(7)

    category2_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
    category2_list = [x for x in category2_list if x.text != '']

    isCategory2First = True
    for idx2 in range(len(category2_list) - 1):
        category2_item = category2_list[idx2]

        if isCategory2First:
            isCategory2First = False
        else:
            category2 = driver.find_elements(By.CLASS_NAME, "its-dropdown")[1]
            category2.click()
            time.sleep(3)

            category2_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
            category2_list = [x for x in category2_list if x.text != '']
            category2_item = category2_list[idx2]

        category2_item.click()
        time.sleep(3)

        category3 = driver.find_elements(By.CLASS_NAME, "its-dropdown")[2]
        category3.click()
        time.sleep(3)

        category3_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
        category3_list = [x for x in category3_list if x.text != '']

        isCategory3First = True

        for idx3 in range(len(category3_list) - 1):
            category3_item = category3_list[idx3]

            if isCategory3First:
                isCategory3First = False
            else:
                category3 = driver.find_elements(By.CLASS_NAME, "its-dropdown")[2]
                category3.click()
                time.sleep(3)

                category3_list = driver.find_elements(By.CLASS_NAME, "v-list-item--link")
                category3_list = [x for x in category3_list if x.text != '']
                category3_item = category3_list[idx3]

            category3_item.click()
            time.sleep(3)

            if isFirst:
                isFirst = False
                loginAndFilterAtFirst()

            table = driver.find_element(By.CLASS_NAME, "its-table-body-wrapper")
            tbody_list = table.find_elements(By.TAG_NAME, "tbody")

            for td in tbody_list:
                td_list = td.find_elements(By.TAG_NAME, "td")
                print([x.text for x in td_list])
                rowId = td.get_attribute("data-id").replace("row-", "")

                csvFile = open("items.csv", "a")
                writer = csv.writer(csvFile)
                writer.writerow([x.text for x in td_list] + [f'https://itemscout.io/keyword?id={rowId}'])
                csvFile.close()
