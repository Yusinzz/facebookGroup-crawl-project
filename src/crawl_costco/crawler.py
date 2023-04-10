from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from facebook_operator import openComment, openViewmore, openReply
import io
import csv
import time

# the destination
url = "https://www.facebook.com/groups/1260448967306807"
# Run in headless mode (without a visible browser window)
options = Options()
# options.add_argument('--headless')
# options.add_argument("--disable-notifications")

driver = webdriver.Chrome(
    executable_path="../crawl-facebook-project/tools/chromedriver", options=options
)
#
cur_height = "return action=document.body.scrollHeight"
try:
    driver.get(url)
except:
    print("url is wrong!")
time.sleep(3)

# post
for x in range(3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("scroll")
    openComment(driver)
    openViewmore(driver)
    openReply(driver)
    time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

posts = soup.find_all("div", class_="x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z")
post_list = []

for idx, post in enumerate(posts):
    print("post")
    print("-" * 30)
    one_post = []
    title_tmp = ""
    comment_tmp = ""
    titles = post.find_all("div", class_="x1iorvi4 x1pi30zi x1swvt13 x1l90r2v")
    if titles:
        for title in titles:
            title_content = title.find_all("div", dir="auto")
            for c in title_content:
                title_tmp += c.text
    if not title_tmp:
        titles = post.find_all("div", class_="x1iorvi4 x1pi30zi x1l90r2v x1swvt13")
        for title in titles:
            title_content = title.find_all(
                "span",
                class_="x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x6prxxf xvq8zen xo1l8bm xzsf02u",
            )
            for c in title_content:
                title_tmp += c.text
    one_post.append(title_tmp)
    print(title_tmp)
    print("-" * 30)
    comments = post.find_all("div", class_="x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r")
    if comments:
        for idx, comment in enumerate(comments):
            comment_content = comment.find("div", dir="auto")
            comment_tmp += f"第{idx+1}則留言:{comment_content.text}/"

    print(comment_tmp)
    one_post.append(comment_tmp)
    post_list.append(one_post)
    print("-" * 30)

with io.open("costco_group_content.csv", "w", encoding="utf_8_sig") as csvfile:
    writer = csv.writer(csvfile, dialect="excel")  # 解決亂碼dialect
    writer.writerow(["發文內容", "留言"])
    for row in post_list:
        writer.writerows([row])
driver.quit()
