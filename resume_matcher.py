import os
import fitz  # PyMuPDF
from preprocess import preprocess_text
from matcher import compute_similarity


def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def match_resume_to_job(job_desc, resume_folder):
    processed_job_desc = preprocess_text(job_desc)
    best_score = -1
    best_resume = None

    for resume_file in os.listdir(resume_folder):
        resume_path = os.path.join(resume_folder, resume_file)

        if resume_file.endswith('.txt'):
            with open(resume_path, 'r', encoding='utf-8') as f:
                resume_text = f.read()
        elif resume_file.endswith('.pdf'):
            resume_text = extract_text_from_pdf(resume_path)
        else:
            continue  # skip unknown formats

        processed_resume = preprocess_text(resume_text)
        score = compute_similarity(processed_job_desc, processed_resume)

        if score > best_score:
            best_score = score
            best_resume = resume_path

    return best_resume, best_score
