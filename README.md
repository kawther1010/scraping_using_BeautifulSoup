# Arabic Fake News Detection Dataset

This repository contains a dataset of Arabic news articles specifically curated for fake news detection purposes. The dataset comprises a mixture of fake and real news articles, categorized by topic, to provide a comprehensive resource for training and evaluating machine learning models.

## Dataset
We have two datasets that are provided in CSV format (`fatabyyano.csv`) and consists of the following columns:

- `title`: Title of the news article
- `time`: The publication date of the article
- `fake or real`: Label indicating whether the article is fake or real
- `topic`: Categorization of the article by topic (e.g., politics, religion, health, etc.)
  
  And (`verify.csv`) and consists of the following columns:

- `Topic d'article`: "The main subject of the article."
- `classification`: "The classification of the article as true or false."
- `Type d'article`: "The type of article, as defined in the HTML content of the page."
- `Arther d'article`: The arther of the article
- `Description d'article`: The description or summary of the article
- `Date de l'article`: The publication date of the article
- `fake or real`: Label indicating whether the article is fake or real

## Scraping Code

The scraping code used to collect the data from reputable Arabic fact-checking websites is available in the `scraping_code` directory. We utilized BeautifulSoup and Selenium for web scraping and parsing HTML content. Separate scripts are provided for each website scraped.

## Report

For detailed information about the project, including methodologies employed, dataset statistics, and other relevant details, please refer to the project report (`report.pdf`) included in this repository.

## Usage

You are welcome to use this dataset for research purposes, particularly in the field of fake news detection and natural language processing. If you find this dataset useful, we kindly request that you cite our work using the provided citation information in the report.

## Contributors

- Nfidsa halima
- Djait ikram
## Contact

For inquiries or further information about this dataset, please contact nfidsahalima@gmail.com
