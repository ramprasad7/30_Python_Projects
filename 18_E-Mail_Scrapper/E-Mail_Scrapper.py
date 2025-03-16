import re
from typing import Final
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


link: str = "https://www.randomlists.com/email-addresses?qty=50"

EMAIL_REGEX: Final[str] = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[
a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[
0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""


class Browser:
    def __init__(self):
        print('Opening Browser...')
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        #self.driver = webdriver.Chrome(self.chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def scrape_emails(self, url: str) -> set:
        print(f"Scraping emails from: {url}")
        self.driver.get(url)
        page_source: str = self.driver.page_source

        list_of_emails: set = set()
        for re_match in re.finditer(EMAIL_REGEX, page_source):
            list_of_emails.add(re_match.group())

        return list_of_emails

    def close_browser(self):
        print("Closing Browser..")
        self.driver.close()

def main():
    browser: Browser = Browser()

    emails: set = browser.scrape_emails(link)

    for i, email in enumerate(emails,start=1):
        print(i, email, sep=': ')
    browser.close_browser()

if __name__ == '__main__':
    main()