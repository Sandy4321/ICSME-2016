# ICSME-ERA Dataset
This document presents the steps needed in order to reproduce the data used in our ICSME-ERA study. Read on for the guidelines.

## Downloading the projects
Here we describe how we download data projects hosted on GitHub.
### ISSUES & PULL-REQUESTS
We have developed two scripts to perform this function, [IssueSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/IssueSpider.py) and [PullSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/PullSpider.py). Both are run through the terminal in a very similar way. See the docstrings in each code to understand it better.

> NOTE: To run these scripts, before install [Scrapy (Installation Guide)](http://doc.scrapy.org/en/latest/intro/install.html) on your machine.

Fill out the question marks with the desired data:

`scrapy runspider [Issue|Pull]Spider.py -a filename = ? -a url = ? -a firstpage = ? -a lastpage = ?`

If you prefer , you can use a similar alternative to download this data in Java , available at:
https://github.com/luizsusin/gitparser

### CONTRIBUTORS & CONTRIBUTIONS

## Generating charts
Here we describe how we generate projects charts.

Before generating graphics, to organize the data collected by the scripts above, we execute four scripts to organize monthly issues, pull-requests, contributors and contributions dates: [IssueMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/IssueMonthlyAmount.py), [PullMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/PullMonthlyAmount.py),
[ContributionMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/ContributionMonthlyAmount.py) and [ContributorMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/ContributorMonthlyAmount.py).

`python [Issue|Pull|Contribution|Contributor]MonthlyAmount.py`


Finally , you can run the script to generate the graphics.




