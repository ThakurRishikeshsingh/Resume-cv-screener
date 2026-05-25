import os
from PyPDF2 import PdfReader

keywords = ["python", "pandas", "sql", "machine learning", "aws"]
resume_path = "./resumes/"

for filename in os.listdir(resume_path):
    if filename.endswith(".pdf"):
        reader = PdfReader(os.path.join(resume_path, filename))
        text = "".join([page.extract_text().lower() for page in reader.pages])
        
        # Count how many keywords are present
        found = [word for word in keywords if word in text]
        score = len(found)
        
        print(f"Candidate: {filename} | Matches: {score}/{len(keywords)} | Skills: {found}")
        
