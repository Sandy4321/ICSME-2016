# ICSME-ERA Dataset
This document presents the steps needed in order to reproduce the data used in our ICSME-ERA study. Read on for the guidelines.

## Downloading the projects
Here we describe how we download data projects hosted on GitHub.
### ISSUES & PULL-REQUESTS
We have developed two scripts to perform this function, [IssueSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/IssueSpider.py) and [PullSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/PullSpider.py). Both are run through the terminal in a very similar way. 
> NOTE: To run these scripts, before install [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html) on your machine.

    scrapy runspider IssueSpider.py -a filename = [file_name] -a url = [project_url] -a firstpage = [first_page_number] -a lastpage = [last_page_number]`



If necessary, see the docstrings in each code to understand it better.


If you prefer , you can use a similar alternative in Java , available at:
https://github.com/luizsusin/gitparser



