from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def openComment(driver):
    try:
        moreComment = driver.find_elements(
            By.XPATH,
            "//div[contains(@class, 'x1i10hfl xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1a2a7pz x6s0dn4 xi81zsa x1iyjqo2 xs83m0k xsyo7zv xt0b8zv')]",
        )
        print(moreComment)
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


def openSeemore(driver):
    try:
        viewmore = driver.find_elements(
            By.XPATH,
            "//div[contains(@class,'x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f') and contains(text(), 'more')]",
        )
        print(viewmore)
        if len(viewmore) > 0:
            count = 0
            for i in viewmore:
                # action = ActionChains(driver)
                try:
                    i.click()
                    # action.move_to_element(i).click().perform()
                    # count += 1
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
