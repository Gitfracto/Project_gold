<img src = "imagen/gold.jpg" width="200" height="200">


# Gold-Project
Gold price, news and other variables!


The objective of this file is to create a MongoDB database that can produce queries linking three different dictionaries linked with the gold commodity

# Readme structure:

1) Our goals
2) Our data cleaning proccess.

## Goals

<img src = "imagen/goal.png" width="200" height="100">


This repository goal is to practice how to extract, transform and load data (ETL). 

### Extract Data
We used three different sources for our data:
[www.dukascopy.com](https://www.dukascopy.com/) We downloaded a csv with the gold prices.
[www.macrotrends.net](https://www.macrotrends.net/) We downloaded a csv with the U.S. monthly interest rate.
[www.reuters.com](https://www.reuters.com/) We scraped the webpage for daily news regarding the gold commodity.

### Transform Data

We used different libraries to transform our data. We will disclose them in the tech stack area of this readme.
You can follow the step by step code in any of the jupyter noteebooks of this repository.

### Load Data

We decided to load the data using MongoDB instead of relational db like mySQL. The main reason was to practice MongoDB structure and queries.

## Tech stack 

-[pandas](https://pandas.pydata.org/docs/)

-[re](https://docs.python.org/3/library/re.html)

[requests](https://docs.python-requests.org/en/latest/)

[bs4](https://pypi.org/project/beautifulsoup4/)

[json](https://docs.python.org/3/library/json.html)

[selenium](https://selenium-python.readthedocs.io/)

[os](https://docs.python.org/3/library/os.html)

[time](https://docs.python.org/3/library/time.html)

[datetime](https://docs.python.org/3/library/datetime.html)


## SRC Folder
<img src = "imagen/python.png" width="200" height="100">


Inside this folder you will be able to hace all the functions that we created in order to clean the data.!

Hope you enjoy the files :)
