import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

CHROME_DRIVER_PATH = "/Users/abdallahal-sarayrah/Development/chromedriver"
url = "https://www.linkedin.com/jobs/search/?currentJobId=3329054359&f_AL=true&geoId=103710677&keywords=python%20developer&location=Jordan&refresh=true"
email = "abdallah.dev85@gmail.com"
password = "Account_1985"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

sign_btn = driver.find_element(By.CSS_SELECTOR, 'a.nav__button-secondary.btn-md.btn-secondary-emphasis')
sign_btn.click()

email_txt = driver.find_element(By.ID, 'username')
email_txt.send_keys(email)

password_txt = driver.find_element(By.ID, 'password')
password_txt.send_keys(password)

login_btn = driver.find_element(By.CSS_SELECTOR, "button.btn__primary--large.from__button--floating")
login_btn.click()

corp_links = driver.find_elements(By.CSS_SELECTOR,
                                  "a.disabled.ember-view.job-card-container__link.job-card-list__title")

for index in range(2):
    time.sleep(0.5)
    corp_links[index].click()
    time.sleep(0.5)
    save_btn = driver.find_element(By.CSS_SELECTOR,
                                   'button.jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary')
    save_btn.click()

menu = driver.find_elements(By.CSS_SELECTOR, "a.app-aware-link.global-nav__primary-link")
jobs_btn = menu[2]
jobs_btn.click()

time.sleep(2)

side_bar = driver.find_elements(By.CSS_SELECTOR,
                                'a.app-aware-link.link-without-hover-state.display-flex.align-items-center')

print(side_bar[0].click())
