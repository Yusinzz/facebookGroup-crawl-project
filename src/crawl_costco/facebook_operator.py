from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def openComment(driver):
    try:
        moreComment = driver.find_elements(
            By.XPATH,
            "//span[contains(@class,'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa')and starts-with(text(), '查看') and contains(text(), '留言')]",
        )
        if len(moreComment) > 0:
            count = 0
            for i in moreComment:
                action = ActionChains(driver)
                try:
                    action.move_to_element(i).click().perform()
                    count += 1
                except:
                    try:
                        driver.execute_script("arguments[0].click();", i)
                        count += 1
                    except:
                        continue
            if len(moreComment) - count > 0:
                print("moreComment issue:", len(moreComment) - count)
            time.sleep(1)
        else:
            pass
    except NoSuchElementException:
        print("need to confirm the moreComment xpath")


def openViewmore(driver):
    try:
        viewmore = driver.find_elements(
            By.XPATH,
            "//div[contains(@class, 'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f')and contains(text(), '顯示更多')]",
        )
        if len(viewmore) > 0:
            count = 0
            for i in viewmore:
                action = ActionChains(driver)
                try:
                    action.move_to_element(i).click().perform()
                    count += 1
                except:
                    try:
                        driver.execute_script("arguments[0].click();", i)
                        count += 1
                    except:
                        continue
            if len(viewmore) - count > 0:
                print("moreComment issue:", len(viewmore) - count)
            time.sleep(1)
        else:
            pass
    except NoSuchElementException:
        print("need to confirm Viewmore the  xpath")


def openReply(driver):
    try:
        moreReply = driver.find_elements(
            By.XPATH,
            "//span[contains(@class,'x193iq5w xeuugli x13faqbe x1vvkbs xlh3980 xvmahel x1n0sxbx x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x3x7a5m x6prxxf xvq8zen x1s688f xi81zsa')and contains(text(), '回覆')]",
        )
        if len(moreReply) > 0:
            count = 0
            for i in moreReply:
                action = ActionChains(driver)
                try:
                    action.move_to_element(i).click().perform()
                    count += 1
                except:
                    try:
                        driver.execute_script("arguments[0].click();", i)
                        count += 1
                    except:
                        continue
            if len(moreReply) - count > 0:
                print("moreComment issue:", len(moreReply) - count)
            time.sleep(1)
        else:
            pass
    except NoSuchElementException:
        print("need to confirm the moreRply xpath")
