# pfd_scrape
This is python script that scrapes pdf bank statements and outputs all incoming funds for the user. The idea is to make it a more dynamic flask application that will scrape and retreive any requested data from a pdf document. 

Currently this works for FNB bank statements (It returns incoming funds activity from the account to help user track their account activity). The next objective is to achieve the same for other major South African banks as well as allowing users to filter incoming/outgoing funds by providing a date range or paayment reference.

In the end, I will create a front end interface which will allow users to upload pdf bank statements and retreive data according to provided filters. The pdf_scraper will be called as REST API endpoint  
