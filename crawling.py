import random

from selenium import webdriver
from selenium.webdriver.common.by import By

month = "6"
day = "19"
proguide_url = "https://proguide.co.kr/best-gaming-monitor/"
keyword = "게이밍 모니터"
keyword_en = "best-gaming-monitor"
itemList = [
    ["LG전자 68.5cm FHD 게이밍 모니터",
     "https://link.coupang.com/a/1v1eQ"],
    ["알파스캔 AOC C27G2 게이밍 144 프리싱크 무결점",
     "https://link.coupang.com/a/1v1n5"],
    ["한성컴퓨터 TFG24F07V 리얼 75 커브드 게이밍 모니터",
     "https://link.coupang.com/a/1v1uu"],
    ["어드밴스원 24인치 FHD 보더리스 리얼 75HZ 모니터",
     "https://link.coupang.com/a/1v1BL"],
    ["어드밴스원 M32Q75P 보더리스 커브드 QHD 75 게이밍",
     "https://link.coupang.com/a/1v1Kw"],
    ["벤큐 조위 61cm FHD BenQ 게이밍 모니터",
     "https://link.coupang.com/a/1v1PT"],
    ["BenQ 모비우스 EX2710 게이밍 무결점",
     "https://link.coupang.com/a/1v1ZZ"],
]
detail_2_contents_order = []
# none:
itemOrdering = [6, 0, 4, 1, 2, 5, 3]

driver = webdriver.Chrome()
driver.get(proguide_url)

title = driver.find_element(By.CLASS_NAME, "entry-title").text
entry_content_list = [x.text for x in driver.find_elements(By.XPATH, "//div/div/p") if x != ""][:4]
detail_1_item_award = [x.text for x in driver.find_elements(By.CLASS_NAME, "ptp-table-award")]
detail_1_item_title = [x.text for x in driver.find_elements(By.CLASS_NAME, "ptp-table-title")]
detail_1_item_feature_list = [[y.get_attribute('outerHTML') for y in x.find_elements(By.TAG_NAME, "li")] for x in
                              driver.find_elements(By.CLASS_NAME, "ptp-table-features-list")]

detail_2_subtitle = [x.text for x in driver.find_elements(By.CLASS_NAME, "heading-list")]
detail_2_contents = [[y.get_attribute('outerHTML') for y in x.find_elements(By.TAG_NAME, "li")] for x in
                     driver.find_elements(By.CLASS_NAME, "arrow-pink")]

detail_3_title = driver.find_element(By.ID, "q2").text
detail_3_intro = [
    [y.get_attribute('outerHTML') for y in x.find_element(By.TAG_NAME, 'ul').find_elements(By.TAG_NAME, 'li')] for x in
    driver.find_elements(By.CLASS_NAME, "product-introduction")]
detail_3_cons = [x.find_element(By.TAG_NAME, 'li').text for x in driver.find_elements(By.CLASS_NAME, "con-box")]
detail_3_table = [x.find_element(By.TAG_NAME, 'table').get_attribute('outerHTML') for x in
                  driver.find_elements(By.CLASS_NAME, "product-spec-table")]

detail_0_ul_hey = ""
for i in itemOrdering:
    detail_0_ul_hey += "<li><a href=\"" + itemList[i][1] + "\"><strong>" + itemList[i][0] + "</strong></a></li>\n"

detail_1_raw = """
    <div class="wp-block-group detail-1-item is-layout-constrained"
    onclick="window.open('DETAIL_1_URL')"
    >
        <div class="wp-block-group__inner-container">
            <p class="detail-1-item-title">DETAIL_1_AWARD</p>
            <p class="detail-1-item-name">DETAIL_1_ITEM_NAME</p>
            <div class="wp-block-group is-nowrap is-layout-flex wp-container-8">
                <figure class="wp-block-image size-full"><img decoding="async" loading="lazy" width="492" height="492"
                                                              src="https://rankguide.co.kr/wp-content/uploads/2023/06/DETAIL_1_IMG_NAME.webp"
                                                              alt="DETAIL_1_ITEM_NAME"
                                                              class="wp-image-5143"
                                                              sizes="(max-width: 492px) 100vw, 492px"></figure>
                <ul>
                    <li>DETAIL_1_FEATURE_1</li>
                    <li>DETAIL_1_FEATURE_2</li>
                    <li>DETAIL_1_FEATURE_3</li>
                </ul>
            </div>
            <div class="detail-1-cta">
              <a>최저가보기</a>
            </div>
        </div>
    </div>"""
detail_1_hey = ""
for i in itemOrdering:
    lastFeature = ""
    if len(detail_1_item_feature_list[i]) > 2:
        lastFeature = detail_1_item_feature_list[i][2]

    detail_1_hey += detail_1_raw.replace("DETAIL_1_AWARD", detail_1_item_award[i]) \
        .replace("DETAIL_1_FEATURE_1", detail_1_item_feature_list[i][0]) \
        .replace("DETAIL_1_FEATURE_2", lastFeature) \
        .replace("DETAIL_1_FEATURE_3", detail_1_item_feature_list[i][1]).replace("DETAIL_1_ITEM_NAME", itemList[i][0]) \
        .replace("DETAIL_1_IMG_NAME", keyword_en + "_" + str(i)).replace("DETAIL_1_URL", itemList[i][1])
    detail_1_hey += "\n"

detail_2_h3_raw = """<h3 class="wp-block-heading"><span class="list-number">INDEX_HEY.</span> SUBTITLE_HEY</h3>\n"""
detail_2_hey = ""
detail_2_content_idx = 0
for i in range(len(detail_2_subtitle)):
    detail_2_hey += detail_2_h3_raw.replace("INDEX_HEY", str(i + 1)).replace("SUBTITLE_HEY", detail_2_subtitle[i][3:])
    if i in detail_2_contents_order:
        now_detail_2_contents = detail_2_contents[detail_2_content_idx]
        random.shuffle(now_detail_2_contents)
        detail_2_hey += '<ul class="arrow-pink styled-list styled-ul-list">' + "\n".join(
            now_detail_2_contents) + "</ul>"
        detail_2_content_idx += 1
    else:
        detail_2_hey += "<p>HEY</p>\n"

detail_3_raw = """
   <div class="wp-block-group is-layout-constrained">
        <div class="wp-block-group__inner-container">
            <h3 class="wp-block-heading detail-3">
                INDEX. DETAIL_3_ITEM_TITLE</h3>
            <div class="wp-block-group detail-3-cta is-layout-constrained" onclick="window.open('DETAIL_3_URL')">
                <div class="wp-block-group__inner-container">
                    <h4 class="wp-block-heading">💡 DETAIL_3_ITEM_AWARD</h4>
                    <figure class="wp-block-image size-full"><a><img
                            decoding="async" loading="lazy" width="492" height="492"
                            src="https://rankguide.co.kr/wp-content/uploads/2023/06/DETAIL_3_IMG_NAME.webp"
                            alt="DETAIL_3_ITEM_TITLE" class="wp-image-5143"
                            sizes="(max-width: 492px) 100vw, 492px"></a></figure>
                    <p class="detail-3-cta-button"><a>최저가 보기</a></p>
                </div>
            </div>
            <ul class="detail-3">
            DETAIL_3_INTRO
              </ul>
            <h4 class="wp-block-heading detail-3-pros" id="10-%EC%9E%A5%EC%A0%90">장점</h4>
            <ul class="detail-3-pros">
                <li>DETAIL_3_FEATURE_1</li>
                <li>DETAIL_3_FEATURE_2</li>
                <li>DETAIL_3_FEATURE_3</li>
            </ul>
            <h4 class="wp-block-heading detail-3-cons" id="11-%EB%8B%A8%EC%A0%90">단점</h4>
            <ul class="detail-3-cons">
                <li>DETAIL_3_CON</li>
            </ul>
            <h4 class="wp-block-heading detail-3-table" id="12-%EC%A0%9C%ED%92%88-%EC%83%81%EC%84%B8%ED%91%9C">제품
                상세표</h4>
            <figure class="wp-block-table detail-3-table">
              DETAIL_3_TABLE
            </figure>
        </div>
    </div>
            """
detail_3_hey = ""
index_hey = 0
for i in itemOrdering:
    detail_3_intro_shuffled = detail_3_intro[i].copy()
    random.shuffle(detail_3_intro_shuffled)
    index_hey += 1

    lastFeature = ""
    if len(detail_1_item_feature_list[i]) > 2:
        lastFeature = detail_1_item_feature_list[i][2]

    detail_3_hey += detail_3_raw.replace("DETAIL_3_URL", itemList[i][1]) \
        .replace("DETAIL_3_ITEM_AWARD", detail_1_item_award[i]) \
        .replace("DETAIL_3_IMG_NAME", keyword_en + "_" + str(i)) \
        .replace("DETAIL_3_ITEM_TITLE", itemList[i][0]) \
        .replace("INDEX", str(index_hey)) \
        .replace("DETAIL_3_INTRO", "\n".join(detail_3_intro_shuffled)) \
        .replace("DETAIL_3_FEATURE_1", detail_1_item_feature_list[i][0]) \
        .replace("DETAIL_3_FEATURE_2", lastFeature) \
        .replace("DETAIL_3_FEATURE_3", detail_1_item_feature_list[i][1]) \
        .replace("DETAIL_3_CON", detail_3_cons[i]) \
        .replace("DETAIL_3_TABLE", detail_3_table[i])

f = open("rank-guide-detail-raw.html", "r")
lines = f.readlines()
replaced_lines = [x.replace("TITLE_HEY", title).replace("KEYWORD_HEY", keyword)
                      .replace("DETAIL_0_UL_HEY", detail_0_ul_hey)
                      .replace("KEYWORD_EN_HEY", keyword_en)
                      .replace("DETAIL_1_HEY", detail_1_hey)
                      .replace("DETAIL_2_HEY", detail_2_hey)
                      .replace("DETAIL_3_HEY", detail_3_hey)
                      .replace("MONTH_HEY", month)
                      .replace("DAY_HEY", day)
                  for x in lines]

f.close()

new_f = open("rank-guide-detail-" + keyword + ".html", "w")
new_f.writelines(replaced_lines)
new_f.close()
