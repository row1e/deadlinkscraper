# deadlinkscraper
Dead link scraper scans a link to find all the dead links within it

Dead Link Checker
This is a Python code snippet that uses the Selenium, BeautifulSoup, Requests, PrettyTable, and csv modules to check for dead links on a website. The code prompts the user to enter a URL, extracts the domain from the URL, and then scans all external links on the page to check if they are alive or dead.

Requirements
Python 3.6 or higher
Selenium 3.141.0 or higher (pip install selenium)
BeautifulSoup 4.9.3 or higher (pip install beautifulsoup4)
Requests 2.25.1 or higher (pip install requests)
PrettyTable 2.1.0 or higher (pip install prettytable)
ChromeDriver executable (download from https://chromedriver.chromium.org/)
Usage
Install the required modules and download the ChromeDriver executable.
Open the Python file in an IDE or text editor.
Update the executable_path variable in line 12 with the path to your Chromedriver executable.
Run the Python file.
Enter a URL when prompted.
Wait for the script to finish scanning all links.
The script will output the results to the console and save the results to a CSV file with the domain and date in the filename.
Note: Make sure to replace the path/to/chromedriver placeholder in the code with the actual path to your Chromedriver executable.
