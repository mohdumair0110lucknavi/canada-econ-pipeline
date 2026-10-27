# Canadian Economy Data Pipeline

A Python data pipeline that collects Canadian economic data from public APIs
(Bank of Canada and Statistics Canada) and organizes it into Bronze, Silver
and Gold layers, so trends like interest rates, inflation and unemployment
can be analyzed together.

Built as a hands-on learning project to practise data engineering
fundamentals: API ingestion, data cleaning, data modelling and automation.

## Data sources

| Source | Data | Frequency |
|---|---|---|
| Bank of Canada Valet API | USD/CAD exchange rate (`FXUSDCAD`) | Daily (business days) |
| Bank of Canada Valet API | Target for the overnight rate (`V39079`) | Daily |
| Statistics Canada Web Data Service | Consumer Price Index, unemployment rate | Monthly |

## Architecture

    APIs  →  Bronze (raw data)  →  Silver (cleaned, validated)  →  Gold (analysis-ready tables)

- **Bronze:** data saved exactly as received from each API
- **Silver:** cleaned, standardized and validated data *(planned)*
- **Gold:** monthly tables combining all series for analysis *(planned)*

## Progress

- [x] Project setup: Python virtual environment, Git, GitHub
- [x] Bronze: ingest Bank of Canada series with a reusable function
- [x] Bronze: ingest Statistics Canada series
- [ ] Silver: clean and validate data
- [ ] Gold: build analysis-ready tables
- [ ] Cloud: move the pipeline to Azure
- [ ] Automation: schedule daily runs

## Tech stack

- Python 3.13
- `requests` for calling APIs
- `pandas` for working with tables
- Git and GitHub for version control

## Project structure

    canada-econ-pipeline/
    ├── data/bronze/        # raw data files (not uploaded to GitHub)
    ├── src/ingest.py       # downloads data from the APIs
    ├── requirements.txt    # Python packages needed
    └── README.md

## How to run

1. Clone the repository:
   `git clone https://github.com/mohdumair0110lucknavi/canada-econ-pipeline.git`
2. Create a virtual environment: `py -V:3.13 -m venv .venv`
3. Activate it: `.venv\Scripts\activate`
4. Install packages: `pip install -r requirements.txt`
5. Create the data folder: `mkdir data\bronze`
6. Run the pipeline: `python src/ingest.py`