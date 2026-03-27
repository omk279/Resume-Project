import streamlit as st
import spacy
import fitz
from skills import TECHNICAL_SKILLS, SOFT_SKILLS

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Page settings
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume to extract skills and get smart suggestions 🚀")

# Extract text from PDF
def extract_text(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text.lower()

# Extract skills
def extract_skills(text):
    tech_found = set()
    soft_found = set()

    for skill in TECHNICAL_SKILLS:
        if skill in text:
            tech_found.add(skill)

    for skill in SOFT_SKILLS:
        if skill in text:
            soft_found.add(skill)

    return list(tech_found), list(soft_found)

# Upload file
uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume uploaded successfully!")

    text = extract_text(uploaded_file)

    if st.button("🔍 Analyze Resume"):

        tech_skills, soft_skills = extract_skills(text)

        # 📊 Dashboard
        st.subheader("📊 Summary")
        col1, col2 = st.columns(2)
        col1.metric("Technical Skills", len(tech_skills))
        col2.metric("Soft Skills", len(soft_skills))

        # 💻 Technical Skills (3 Columns)
        st.subheader("💻 Technical Skills")

        if tech_skills:
            cols = st.columns(3)
            for i, skill in enumerate(tech_skills):
                cols[i % 3].markdown(f"✅ **{skill.title()}**")
        else:
            st.warning("No technical skills found")

        # 🧠 Soft Skills (2 Columns)
        st.subheader("🧠 Soft Skills")

        if soft_skills:
            cols = st.columns(2)
            for i, skill in enumerate(soft_skills):
                cols[i % 2].markdown(f"🟢 {skill.title()}")
        else:
            st.warning("No soft skills found")

        # 🎯 Resume Score
        tech_score = len(tech_skills) * 5
        soft_score = len(soft_skills) * 3
        total_score = min(tech_score + soft_score, 100)

        st.subheader(f"📈 Resume Score: {total_score}/100")

        if total_score > 70:
            st.success("🔥 Strong Resume!")
        elif total_score > 40:
            st.info("👍 Average Resume")
        else:
            st.warning("⚠️ Needs Improvement")

        # 🎯 Suggestions
        st.subheader("🎯 Suggestions to Improve Resume")

        suggestions = []

        important_skills = ["python", "sql", "machine learning", "data analysis"]

        for skill in important_skills:
            if skill not in tech_skills:
                suggestions.append(f"👉 Consider adding **{skill.title()}**")

        if len(soft_skills) < 3:
            suggestions.append("👉 Add more soft skills like Communication, Leadership")

        if "project" not in text:
            suggestions.append("👉 Include project experience for better impact")

        if "internship" not in text:
            suggestions.append("👉 Mention internship experience if available")

        if suggestions:
            for s in suggestions:
                st.info(s)
        else:
            st.success("🚀 Excellent Resume! No major improvements needed")