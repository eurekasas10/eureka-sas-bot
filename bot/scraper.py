import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EurekaSASScraper:
    def __init__(self, base_url, headless=True):
        self.base_url = base_url
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def login(self, username, password):
        self.driver.get(self.base_url)
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-btn")
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "question")))

    def extract_questions(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        questions = soup.find_all('div', class_='question')
        questions_list = []
        for q in questions:
            question_id = q.get('data-id', '')
            question_text = q.find('span', class_='question-text')
            if question_text:
                questions_list.append({'id': question_id, 'text': question_text.get_text(strip=True), 'element': q})
        return questions_list

    def close(self):
        self.driver.quit()