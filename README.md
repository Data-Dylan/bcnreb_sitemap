# BC Real Estate Board Sitemap
This is an old python script I made to understand web crawlers. It generates a sitemap for the BC Northern Real Estate Board's website. Basic web crawlers could be used in ways that many do not consider. For example, an adapted script could be used with a CRON job to determine when dead links occur on a website.

## General Information
Web crawlers are distinct algorithms in that they use recursive-logic to find all the hyperlinks on a website. For each hyperlink the algorithim finds, it visits that hyperlink and finds all the hyperlinks on that page. To avoid running infinitly, a [set](https://www.w3schools.com/python/python_sets.asp) data structure is used so that web pages are not redundantly updated. 

## Credit
This python script uses re-adapted concepts used in [Web Scraping with Python: Collecting Data from the Modern Web](https://www.goodreads.com/book/show/25752783-web-scraping-with-python) by Ryan Mitchell.
