from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
from prettytable import PrettyTable
import csv
from urllib.parse import urlparse
from datetime import datetime

# set up Chrome options to enable JavaScript
options = Options()
options.add_argument("--enable-javascript")

# set up Chrome driver
s = Service(executable_path='path/to/chromedriver') # replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=s, options=options)

url = input("Enter a URL: ")

# Extract the domain from the URL
parsed_url = urlparse(url)
domain = parsed_url.netloc

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

driver.get(url)  # load the URL in the browser
time.sleep(5) # wait for the page to load

# get the page source after the JavaScript has loaded
html = driver.page_source

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# find all <a> tags on the page
links = soup.find_all('a')

# extract the href attribute from each <a> tag and store it in a list
hrefs = []
for link in links:
    href = link.get('href')
    if href and href.startswith('http'):  # only check external links
        hrefs.append(href)

# check if each link is alive or dead
results = {}
for i, href in enumerate(hrefs):
    try:
        print(f"Scanning {i+1}/{len(hrefs)}: {href}")
        response = requests.get(href, timeout=10)
        if response.status_code < 400 and response.headers.get('content-type') is not None:
            status = f"Working ({response.status_code})"
        else:
            status = f"Dead? ({response.status_code})"
        if status not in results:
            results[status] = []
        results[status].append(href)
        print(f"  Result: {status}")
    except (requests.exceptions.RequestException, requests.exceptions.Timeout):
        if "Dead Link" not in results:
            results["Dead Link"] = []
        results["Dead Link"].append(href)
        print(f" Result: Dead Link (Timeout or Request Exception)")

# create a table for the results
table = PrettyTable(['Link', 'Status'])
for status, links in results.items():
    for link in links:
        if status.startswith("Dead"):
            table.add_row([f"\033[31m{link}\033[0m", status])
        else:
            table.add_row([link, status])

# print the table
print(str(table))

# Save the results to a CSV file with the domain and date in the filename
csv_filename = f"dead_link_checker_results_{domain}_{current_date}.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Write the header row
    csv_writer.writerow(['Link', 'Status'])

    # Write the data rows
    for status, links in results.items():
        for link in links:
            csv_writer.writerow([link, status])

print(f"Results saved to {csv_filename}")

driver.quit()  # close the browser
