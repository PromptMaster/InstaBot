from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from random import randint
import time
import globals


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge(executable_path=r'C:\Users\Promp\Documents\msedgedriver\msedgedriver.exe')

    def login(self): #Log in your instagram account

        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(randint(2, 5))
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(randint(8, 12))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        time.sleep(randint(7, 13))
        self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()

    def like_picshashtag(self, hashtag, br): #Leave a like on the photos from the hashtags located in "globals" file

        driver = self.driver
        time.sleep(randint(5, 7))
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(randint(8, 10))
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(randint(3, 4))

        time.sleep(4)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' Photos: ' + str(len(pic_hrefs)))

        n = 1
        for pic_href in pic_hrefs:
            if br == 0:
                if n < len(pic_hrefs) - 16:
                    driver.get(pic_href)
                    time.sleep(5)
                    try:
                        if self.isitliked(1) == 0:
                            try:
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                                print('Pic ' + str(n) + ' liked')
                            except NoSuchElementException:
                                print("error: no such element")
                                break
                        n = n + 1
                        if randint(1, 30) > 27:
                            breaktime = randint(8, 25)
                            print('Short Break! Back in ' + str(breaktime) + ' Seconds!')
                            time.sleep(breaktime)
                        else:
                            time.sleep(randint(6, 12))
                    except Exception as e:
                        time.sleep(5)
                else:
                    n = n + 1
                    break
            if br == 1:
                if n < len(pic_hrefs) - 30:
                    if n > 10:
                        driver.get(pic_href)
                        time.sleep(5)
                        try:
                            if self.isitliked(1) == 0:
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button").click()
                                print('Pic ' + str(n - 10) + ' liked')
                            n = n + 1
                            if randint(1, 30) > 27:
                                breaktime = randint(8, 20)
                                print('Short Break! Back in ' + str(breaktime) + ' Seconds!')
                                time.sleep(breaktime)
                            else:
                                time.sleep(randint(6, 12))
                        except Exception as e:
                            time.sleep(5)
                    else:
                        n = n + 1
                else:
                    n = n + 1
                    break

    def like_followings(self): #Leave a like on photos from the people you follow

        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(randint(2, 5))
        for i in range(1, 5):
            likebutton = driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/section/div/div[2]/div/article[" + str(i) + "]/div[3]/section[1]/span[1]/button")
            if self.isitliked(i) == 0:
                href = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[" + str(i) + "]/header/div[2]/div[1]/div/span/a")
                likebutton.click()
                print('Pic ' + str(i) + ' liked: ' + str(href.text))
                time.sleep(randint(5, 10))
            else:
                nextpic = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/section/div/div[2]/div/article[" + str(i) + "]/div/div[3]/section[1]/span[1]/button")
                self.driver.execute_script('arguments[0].scrollIntoView()', nextpic)
                time.sleep(randint(1, 3))

        for j in range(5, 70):
            try:
                likebutton = driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/section/div/div[2]/div/article[5]/div[3]/section[1]/span[1]/button")
                if self.isitliked(5) == 0:
                    href = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div/div[2]/div/article[5]/header/div[2]/div[1]/div/span/a")
                    likebutton.click()
                    print('Pic ' + str(j) + ' liked: ' + str(href.text))
                    if randint(1, 20) > 19:
                        breaktime = randint(15, 30)
                        print('Short Break! Back in ' + str(breaktime) + ' Seconds!')
                        time.sleep(breaktime)
                    else:
                        time.sleep(randint(5, 10))
                else:
                    nextpic = self.driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/section/div/div[2]/div/article[5]/div[3]/section[1]/span[1]/button")
                    self.driver.execute_script('arguments[0].scrollIntoView()', nextpic)
                    time.sleep(randint(0, 2))
            except (NoSuchElementException, ElementClickInterceptedException):
                time.sleep(randint(5, 6))
                nextpic = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/section/div/div[2]/div/article[5]/div[3]/section[1]/span[1]/button")
                self.driver.execute_script('arguments[0].scrollIntoView()', nextpic)
                continue

    def unfollowfollow(self, user): #unfollow and then follow again famous people (it gets you some followers sometime)
        time.sleep(randint(2, 4))
        driver = self.driver
        try:
            driver.get('http://www.instagram.com/' + user)
            time.sleep(randint(4, 7))
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div[2]/button').click()
                time.sleep(randint(1, 3))
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                time.sleep(randint(2, 4))
            except:
                print('error: unfollow button not found for ' + user)
            
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/button').click()
            except:
                print('error: follow button not found for ' + user)

            print(user + ' Followed')
        except:
            print('error: user ' + user + ' not found')
        time.sleep(randint(4, 7))

    def isitliked(self, article): #checks it a photo has been already liked

        driver = self.driver
        try:
            driver.find_element_by_css_selector("article:nth-of-type(" + str(article) + ") svg[aria-label^='Descurt']")
            print('Pic Already Liked')
            return 1
        except NoSuchElementException:
            driver.find_element_by_css_selector("article:nth-of-type(" + str(article) + ") svg[aria-label^='Curti']")
            return 0

    def followcloseppl(self): #follow some close random people (unfinished)

        driver = self.driver
        driver.get('http://www.instagram.com/' + self.username)
        time.sleep(randint(3, 6))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(randint(3, 4))
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            """, scroll_box)

    def follow_suggestions(self): #follow people from instagram suggestions

        driver = self.driver
        for i in range(1, 100):
            driver.get('https://www.instagram.com/explore/people/suggested/')
            time.sleep(randint(2, 5))
            if i > 28:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(randint(2, 4))
            if i > 58:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(randint(2, 4))
            if i > 88:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(randint(2, 5))

            try:
                user = str(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[" + str(i) + "]/div[2]/div[1]/div/span/a").text)
            except:
                print("user not found")            
            try:
                driver.get('https://www.instagram.com/' + user + '/')
            except:
                print(user + "user page not found")
            time.sleep(randint(2, 5))
            try:
                pubs_number = int(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[1]/span/span").text)
            except:
                print("error: number of publications not found")
            try:
                followers_number = int(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]/span/span").text) #Private account
            except:                                                
                followers_number = int(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]/a/span").text) #Non Private Account            
            try:
                user_name = str(driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/h1").text).split()[0]
            except:
                print("error: name not found")


            if (pubs_number > 6) and (followers_number > 100):
                try:
                    self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/button').click()
                    print(user + 'FOLLOWED')
                    i = i - 1    
                except:    
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button').click()
                        print(user + 'FOLLOWED')
                        i = i - 1    
                    except:
                        print('error: follow button not found for ' + user)
                    
            else:
                print(user + " not followed")

            time.sleep(randint(2, 5))


fakopolisBot = InstaBot('', '') #put your Instagram username on the first '' and your password on the second ''
fakopolisBot.login()

for hashtag in globals.hts:
    fakopolisBot.like_picshashtag(hashtag, 0)

fakopolisBot.like_followings()
fakopolisBot.follow_suggestions()

for hashtag in globals.htsbr:
    fakopolisBot.like_picshashtag(hashtag, 1)

for ppl in globals.famous:
    fakopolisBot.unfollowfollow(ppl)


