# y_footy_analytics_tho

The purpose of y_footy_analytics_tho is to have a data visualisations that can show me trends and outliers based on football leagues to make
better decisions for my FPL, which will help others who want to attain a competive edge to their teams transfers and selsction.

The intention is to build various iterations of this web-based platform. For version 1.0 I itend to use the following technolgies to build the platform:
- Python (Programming langauge)
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
