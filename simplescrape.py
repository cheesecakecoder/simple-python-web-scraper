import requests

url = "http://webscrapingscripts.com/"
extract_from = "<title>";
extract_to = "</title>";

page = requests.get(url)

if page.status_code == 200:
    print page.content
    print "\r\n"
    title = page.content[page.content.find(extract_from)+len(extract_from):page.content.find(extract_to)]
    print "The scraped title is: " + title + "\r\n"
else:
    print "Error: Page did not return expected 200 OK\r\n"

    
