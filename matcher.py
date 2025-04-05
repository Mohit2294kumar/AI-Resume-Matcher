# matcher.py
import os
import pandas as pd
import json

def parse_job_data(raw_text):
    lines = raw_text.strip().split('\n')
    jobs = []
    for line in lines:
        if '\t' in line:
            title, description = line.split('\t', 1)
            jobs.append({"Job Title": title.strip(), "Job Description": description.strip()})
    return jobs

def save_data(jobs, csv_path='data/job_data.csv', json_path='data/job_data.json'):
    df = pd.DataFrame(jobs)
    df.to_csv(csv_path, index=False)
    with open(json_path, 'w') as f:
        json.dump(jobs, f, indent=2)

def load_jobs(csv_path='data/job_data.csv'):
    return pd.read_csv(csv_path)

if __name__ == "__main__":
    with open("data/raw_data.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    jobs = parse_job_data(raw_text)
    save_data(jobs)
    print("✅ Job data saved to CSV and JSON.")
    
    
    def load_jobs(csv_path="data/jobs.csv"):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"📁 File not found: {csv_path}. Make sure it's in your GitHub repo.")
        return pd.read_csv(csv_path)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

