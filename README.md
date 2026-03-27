📄 AI Resume Analyzer

An intelligent web application that analyzes resumes using Natural Language Processing (NLP) to extract skills and provide improvement suggestions.

🚀 Features
Upload Resume (PDF)
Extract Technical Skills
Extract Soft Skills
Resume Scoring System
Smart Suggestions for Improvement
Skill Summary Dashboard
🛠️ Tech Stack
Python
Streamlit (UI)
spaCy (NLP)
PyMuPDF (PDF processing)
⚙️ How It Works
User uploads resume in PDF format
System extracts text from the document
NLP processes the text
Skills are identified and categorized
Resume score is calculated
Suggestions are provided to improve the resume
📊 Example Output

Input Resume:
Skilled in Python, SQL, Machine Learning, Leadership

Output:
Technical Skills:
✔ Python
✔ SQL
✔ Machine Learning

Soft Skills:
✔ Leadership

Resume Score: 35/100

🧪 Run Locally

pip install streamlit spacy PyMuPDF
python -m spacy download en_core_web_sm
streamlit run app.py

🎯 Future Improvements
Job Role Matching (AI-based)
Resume Ranking System
Graphical Skill Visualization

👨‍💻 Author

Omkar Keny

💡 Note

This project is developed as part of a Self Learning Activity (SLA) to demonstrate the use of NLP in real-world applications such as recruitment systems.
