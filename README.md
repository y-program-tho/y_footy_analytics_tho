# Y Footy Analytics (FPL Helper)

A data-driven web application designed to help Fantasy Premier League (FPL) managers make better decisions for their team selections and transfers by providing insightful visualizations of football statistics and trends.

## Overview

Y Footy Analytics automatically scrapes and analyzes football data from FBref, presenting it through an intuitive web interface. The platform helps users identify trends and outliers in football statistics, giving FPL managers a competitive edge in their decision-making process.

## Features

- Automated data collection from FBref
- League-wide statistical analysis
- Team performance tracking
- Player statistics visualization
- Interactive dashboards for data exploration
- FPL-focused insights and metrics

## Technologies Used

### Core Technologies
- Python (Programming language)
- Streamlit (Web-based dashboards for data visualization)
- Pandas (Data cleaning, mining, and aggregation)
- Matplotlib + Seaborn (Data visualization)
- Python Google Sheets API (Data storage and warehousing)
- BeautifulSoup4 (Web scraping)

Additional dependencies can be found in the `requirements.txt` file.

## Project Structure

```
y_footy_analytics_tho/
├── main.py                 # Main application entry point
├── fbref_batch_scraper.py # Data scraping functionality
├── pages/                 # Streamlit pages
│   ├── 1_team.py         # Team analysis dashboard
│   └── 2_player.py       # Player analysis dashboard
└── requirements.txt      # Project dependencies
```

## Getting Started

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```

## Feedback and Contributions

This is version 1.0 of the platform. We welcome any feedback, suggestions, or contributions for future versions. Please feel free to:
- Open an issue for bugs or feature requests
- Submit pull requests for improvements
- Share ideas for version 2.0 features

## Note

This tool is designed to assist in FPL decision-making but should be used in conjunction with your own research and intuition.

Happy FPL managing! 😊
