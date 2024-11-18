# jobs/scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time

def scrape_jobs():
    url = "https://www.indeed.com/jobs?q=Python+developer"
    
    # Set up Selenium with Chrome
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run in headless mode
    service = Service('/home/pandeyganesha/codes/python/indeed_scraper/indeed_scraper/jobs/chromedriver-linux64/chromedriver')  # Updated path to ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    
    jobs = []

    # Find all job cards
    for job_card in soup.find_all('div', class_='job_seen_beacon'):
        # import pdb; pdb.set_trace()
        title = job_card.find('h2', class_='jobTitle').text.strip()
        # company = job_card.find('span', class_='companyName').text.strip()
        # location = job_card.find('div', class_='companyLocation').text.strip()
        # salary = job_card.find('div', class_='salary-snippet')
        # salary = salary.text.strip() if salary else None
        # description = job_card.find('div', class_='job-snippet').text.strip()
        # url = "https://www.indeed.com" + job_card.find('a')['href']
        company = location = salary = description = url = 'N/A'
        jobs.append({
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
            'description': description,
            'url': url,
        })

    client = MongoClient('localhost', 27017)
    db = client['indeed_scraper']
    collection = db['jobs']
    collection.insert_many(jobs)

if __name__ == "__main__":
    scrape_jobs()