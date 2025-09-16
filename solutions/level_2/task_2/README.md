# Data Scrapper - Level 2 Task 2

This application scrapes headlines from [Hacker News](https://news.ycombinator.com/) and saves them to a CSV file.

## Features

- Fetches the latest headlines from Hacker News.
- Saves headlines to `headlines.csv` in the current directory.
- Simple and easy to use.

## Files

- [`data_scrapper.py`](data_scrapper.py): Main script for scraping headlines.
- [`headlines.csv`](headlines.csv): Output file containing the scraped headlines.
- [`requirements.txt`](requirements.txt): Python dependencies for the project.

## Usage

1. **Install dependencies**  
   Make sure you have Python 3.10+ and install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the scraper**
   ```sh
   python data_scrapper.py
   ```

   This will fetch the headlines and save them to `headlines.csv`.

## Customization

You can change the target URL by passing it as an argument to the `scrape_headlines` function in [`data_scrapper.py`](data_scrapper.py).

## Example Output

See [`headlines.csv`](headlines.csv) for a sample of the scraped headlines.

## Environment

A Python virtual environment is included in the `.env` directory for dependency isolation.

---

*This project is for educational purposes as part of Level 2, Task