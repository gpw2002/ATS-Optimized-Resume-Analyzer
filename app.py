import streamlit as st
import google.generativeai as genai
import os
import json
import requests
import docx2txt # type: ignore
import PyPDF2 as pdf
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import time

# Load environment variables from a .env file
load_dotenv()

# Configure the generative AI model with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model configuration for text generation
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# Define safety settings for content generation
safety_settings = [
    {"category": f"HARM_CATEGORY_{category}", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
    for category in ["HARASSMENT", "HATE_SPEECH", "SEXUALLY_EXPLICIT", "DANGEROUS_CONTENT"]
]


def generate_response_from_gemini(input_text):
    llm = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    output = llm.generate_content(input_text)
    return output.text


def extract_text_from_pdf_file(uploaded_file):
    pdf_reader = pdf.PdfReader(uploaded_file)
    text_content = ""
    for page in pdf_reader.pages:
        text_content += page.extract_text()
    return text_content


def extract_text_from_docx_file(uploaded_file):
    return docx2txt.process(uploaded_file)


# Prompt Template
input_prompt_template = """
As an experienced Applicant Tracking System (ATS) analyst,
with profound knowledge in technology, software engineering, data science, full stack web development, cloud engineering, 
cloud developers, devops engineering, and big data engineering, your role involves evaluating resumes against job descriptions.
Recognizing the competitive job market, provide top-notch assistance for resume improvement.
Your goal is to analyze the resume against the given job description, 
assign a percentage match based on key criteria, and pinpoint missing keywords accurately.
resume:{text}
description:{job_description}
I want the response in one single string having the structure
{{"Job Description Match":"%","Missing Keywords":"","Candidate Summary":"","Experience":""}}
"""

# Streamlit app

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200: 
        return None
    return r.json() 

lottie_checking = load_lottiefile("assets/checking.json")

# Page Configuration
st.set_page_config(page_title="ATS-Resume Analyzer", layout="centered")

# Page Title and Instructions
st.title("🚀 Track My Resume 🚀")
st.markdown("""
    <style>
    h1 {
        color: #FF9800;
        text-align: center;
        font-family: Poppins, sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

st.subheader("📄 ATS-Optimized Resume Analyzer")
st.write("Upload your resume and the job description, and we'll provide an ATS analysis including match score and keyword recommendations.")

# Job Description Input
job_description = st.text_area("📝 Paste the Job Description", height=200, help="Enter the job description for analysis.")

# Resume Upload Section
uploaded_file = st.file_uploader("📂 Upload Your Resume", type=["pdf", "docx"], help="Please upload a PDF or DOCX file")

# Action Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    check_button = st.button("🔍 Check ATS Result")
with col2:
    score_button = st.button("📊 Check Score")
with col3:
    info_button = st.button("ℹ️ How It Works")

# Processing Logic
if check_button or score_button:
    if uploaded_file and job_description:
        st.lottie(lottie_checking, speed=1, loop=True, height=150, width=150)

        # Extract Resume Text
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf_file(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx_file(uploaded_file)

        # Generate Response from Gemini Model
        response_text = generate_response_from_gemini(input_prompt_template.format(text=resume_text, job_description=job_description))

        # Extract and Display Match Percentage
        match_percentage_str = response_text.split('"Job Description Match":"')[1].split('"')[0]
        match_percentage = float(match_percentage_str.rstrip('%'))

        # Display ATS Evaluation Results
        st.markdown('<h3 style="color: #FFEB3B;">ATS Evaluation Result</h3>', unsafe_allow_html=True)

        if match_percentage >= 80:
            st.markdown('<p style="color: green;">👍 Move forward with hiring!</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p style="color: red;">👀 More work needed to improve your resume!</p>', unsafe_allow_html=True)

        # Score Display
        if score_button:
            st.markdown('<h3 style="color: #FFEB3B;">Your ATS Score</h3>', unsafe_allow_html=True)
            st.write(f"💼 **{match_percentage_str}%** match with the job description.")
    else:
        st.warning("⚠️ Please upload both your resume and the job description to proceed.")

# Information Section
if info_button:
    st.write("""
    **How It Works:**
    1. Upload your resume as a PDF or DOCX file.
    2. Paste the job description for which you're applying.
    3. Get an ATS match percentage and tips to improve your resume.
    """)
    st.lottie(lottie_checking, speed=1, loop=True, height=150, width=150)

# Footer
st.text(" ")
st.markdown("""
    <div style='text-align: center; font-size: small;'>
        Developed by <a href="https://github.com/gpw2002" target="_blank" style="color: yellow;">Gaurav Wani</a>
    </div>
""", unsafe_allow_html=True)
