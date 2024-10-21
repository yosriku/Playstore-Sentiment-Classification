# Playstore Sentiment Classification

This repository contains the implementation of a sentiment classification model for Google Play Store reviews. The project involves scraping reviews from the Play Store, processing the data, and training a machine learning model to classify the sentiment of the reviews.

## Repository Structure

- **`scraping.py`**: Script to scrape reviews from the Google Play Store using the `google-play-scraper` library.
- **`Another_copy_of_Sentiment_Analysis_Dicoding (2).ipynb`**: Jupyter Notebook for data preprocessing, model training, and evaluation.
- **`playstore_reviews.csv`**: Sample dataset containing reviews scraped from the Play Store.
- **`sentiment_model/`**: Directory containing the saved sentiment model.
- **`requirements.txt`**: List of dependencies required to run the project.

## Setup Instructions

### 1. Create a Virtual Environment

To isolate the project dependencies, it’s recommended to create a virtual environment:

```terminal
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
# or
venv\Scripts\activate  # For Windows
```

### 2. Install Dependencies

Once the virtual environment is activated, install the necessary libraries using the requirements.txt file:

```terminal
pip install -r requirements.txt
```

### 3. Customize Scraping Settings

Customize application id, fore example com.game.test

### 4. Run the Jupyter Notebook

Run Jupyter Notebook in local or using Google Collab, then upload the playstore_reviews.csv into /content/dataset/

