# ICSME-ERA Dataset
This document presents the steps needed in order to reproduce the data used in our ICSME-ERA study. Read on for the guidelines.

## Downloading Data
Here we describe how we download projects data from GitHub.
#### ISSUE AND PULL-REQUEST 
We have developed two scripts to perform this function, [IssueSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/IssueSpider.py) and [PullSpider.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/PullSpider.py). Both are run through the terminal in a very similar way. Follow the model below and see the docstrings in each code to understand it better:

> NOTE: To run these scripts, before install [Scrapy](http://doc.scrapy.org/en/latest/intro/install.html) on your machine.

```bash
  scrapy runspider [Issue|Pull]Spider.py -a filename = project_data.txt -a url = https://github.com/ruby/ruby/ -a firstpage = 1 -a lastpage = 10
```
At the end of the program , you must have a file like [this](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/issue_file_example.txt). If you prefer , you can use a similar alternative to download this data in Java , available at:
https://github.com/luizsusin/gitparser

#### CONTRIBUTOR AND CONTRIBUTION
Initially , clone the repository as in the example below:

``` git clone https://github.com/ruby/ruby.git```

Then run the shellscripts [Contributors.sh](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/Contributors.sh), [Contributions.sh](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/Contributions.sh), [Newcomers.sh](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/Newcomers.sh) as follows:

``` ./[Contributors|Newcomers].sh /home/example/repository ```

``` ./Contributions.sh (Run this code in the repository folder) ```

## Generating charts
Before generating charts, to organize the data collected by the scripts above, we execute four scripts to organize monthly issues, pull-requests, contributors and contributions dates: [IssueMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/IssueMonthlyAmount.py), [PullMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/PullMonthlyAmount.py),
[ContributionMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/ContributionMonthlyAmount.py) and [ContributorMonthlyAmount.py](https://github.com/fronchetti/ICSME-ERA-Dataset/blob/master/ContributorMonthlyAmount.py).

To perform each of the codes, use:

` python [Issue|Pull|Contribution|Contributor]MonthlyAmount.py`

Finally , you can run the script to generate the graphics.




