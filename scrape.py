from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

# Replace with the path to your chromedriver executable
chromedriver_path = '/Users/louisamayhanrahan/louscode/scrape/chromedriver/chromedriver'

# Set up the Selenium WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

# Set an implicit wait time
driver.implicitly_wait(60)

# Open the webpage
url = 'https://sam.gov/search/?page=1&pageSize=25&sort=-modifiedDate&index=opp&sfm%5BsimpleSearch%5D%5BkeywordRadio%5D=ALL&sfm%5Bstatus%5D%5Bis_active%5D=true&sfm%5BawardeeDetails%5D%5Bstate%5D%5B0%5D%5Bkey%5D=CA&sfm%5BawardeeDetails%5D%5Bstate%5D%5B0%5D%5Bvalue%5D=CA%20-%20California'
driver.get(url)

# Wait for the page to fully render (increase if necessary)
driver.implicitly_wait(10)

# Get page source after JavaScript has rendered the content
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract all text from the page
all_text = soup.get_text(separator='\n')

# Print the text or save it to a file
print(all_text)

# Optionally, save the text to a file
with open('scraped_text.txt', 'w', encoding='utf-8') as file:
    file.write(all_text)


