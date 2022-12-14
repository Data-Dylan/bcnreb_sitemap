"""
This purpose of this program is to create a program-generated sitemap for the
BC Northern Real Estate's website. This program was created to gain a stronger
understanding of web crawlers.
"""
# Libraries used.
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import re
from time import sleep
from pprint import pprint

# Regular expression to find BCNREB URLs on page.
url_regex = re.compile(r"http://(www.)?bcnreb.bc.ca|^/")

# Function to get BCNREB URLs on page.
def url_return(url):
    
    # Use global defined variable.
    global url_regex
    
    # Request data from url of website.
    html = urlopen(url)
    
    # Parse HTML for home page.
    soup = bs(html, "html.parser")
    
    # Find ancor tags for BCNREB URLs.
    tags = soup.find_all("a", href = url_regex)

    # Loop to clean tags for consistancy.
    for index, tag in enumerate(tags):
        tag = tag.attrs["href"]
        tag = tag.replace("www.", "")
        tag = tag.replace(" ", "%20")
        
        # Add domain name if it is not included.
        if base_url not in tag:
            tag = base_url + tag
            
        tags[index] = tag
    
    # Return list of URLs.
    return list(tags)

# URL of the home of the website.
base_url = "http://bcnreb.bc.ca"

# Create set object to populate.
unique_urls = set()

# Regular expression to detect file extensions.
ext_regex = re.compile(r"\.[a-z]{3}$", re.I)

# Function to scrape URLs, and generate BCNREB sitemap.
def sitemap(base_url):
    
    # Use global defined variable.
    global unique_urls
    
    # Create list of URLs from home page.
    page_list = url_return(base_url)
        
    # Iterate through URL list for sitemap generation.
    for page in page_list:
        
        # Test if URL is in sitemap already.
        if page not in unique_urls:
            
            # Add to sitemap.
            print(page + " was added to the sitemap.")
            unique_urls.add(page)
            
            # Skip requesting URLs with file extensions.
            if bool(ext_regex.search(page)):
                print("File extension detected.")
                print("Continuing...")
                print("")
                continue
            
            # Scraper pause.
            sleep(2)
            
            # Recursive call to get URLs from page that was added.
            try:
                print("Checking " + page + " for URLs...")
                print("")
                sitemap(page)
            except HTTPError:
                print("Http error. Removed url from sitemap")
                unique_urls.remove(page)
                
                                
        # Print message, and go to next loop iteration.
        else:
            print (page + " is already in the sitemep.")
            print("Continuing...")
            print("")
    
    # Return sitemap. 
    return unique_urls

# Look at output
links = sitemap(base_url)
pprint(links)

