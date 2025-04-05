# Job Description Explorer

This Streamlit app parses and visualizes structured job descriptions.

## Structure

```
data/
├── job_data.csv          # Exported structured CSV
├── job_data.json         # Exported structured JSON
├── raw_data.txt          # Optional: raw tab-separated job data

templates/                # Optional (not used in Streamlit)

app.py                    # Streamlit app
matcher.py                # Parser and exporter
preprocess.py             # Helper functions
requirements.txt
.gitignore
README.md
```

## Setup

```bash
pip install -r requirements.txt
python matcher.py
streamlit run app.py
```
