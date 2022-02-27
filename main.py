from selenium import webdriver
import time
from userInfo import username, password

class Trello:
    # takes weekly jobs from trello

    def __init__(self, username, password ):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.job_list = []

    def signIn(self):
        # sign in system
        self.browser.get("https://trello.com/")
        self.browser.find_element_by_xpath("/html/body/header/nav/div/a[1]").click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='user']").send_keys(f"{self.username}")
        self.browser.find_element_by_xpath("//*[@id='login']").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(f"{self.password}")
        self.browser.find_element_by_xpath("//*[@id='login-submit']/span").click()
        time.sleep(2)
     
    def extoErp(self):
        """
        must be take every job from cards. entry links and take pop-up title
        """
        self.browser.get("https://trello.com/b/26vNhN5s/exto-erp")
        time.sleep(1)
        x = self.browser.find_elements_by_css_selector(".js-list")[1]
        list = x.find_element_by_class_name("list-cards").find_elements_by_class_name("list-card")
        for href in list:
            self.job_list.append(href.find_element_by_css_selector(".list-card-title").text)
        
    def jobListView(self):
        x = 0
        for i in self.job_list:
            print(f"-{x+1} {i}")
            x = x+1

    def writeFile(self):
        with open("maddeler.txt", "w", encoding="utf-8") as f:
            for i in self.job_list:
                f.write(f"- {i}\n")
            f.close()




x = Trello(username,password)
x.signIn()
x.extoErp()
x.jobListView()
x.writeFile()