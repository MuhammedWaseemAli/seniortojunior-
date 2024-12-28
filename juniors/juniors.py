import streamlit as st
import matplotlib.pyplot as plt
import random
import pandas as pd
import altair as alt
from streamlit_lottie import st_lottie
import requests

whats_new = [
    "Updated Madhav sir's lecture in PCP. Focus on it at the end when advanced topics are covered.",
    "Updated PCP textbooks: Peavy and Benefield are referred.",
    "EMDA question papers added.",
    "SWM textbooks and PPT uploaded.",
    "PCP 2019 question paper added to quiz folder."
]

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_book = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

# Global styling
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
        color: #343a40;
    }

    .main {
        padding: 20px;
    }

    .stButton>button {
        color: #ffffff;
        background-color: #007bff;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        transition: background-color 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        background-color: #0056b3;
    }

    .resource-card {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border: 1px solid #ddd;
        transition: transform 0.3s ease-in-out;
    }

    .resource-card:hover {
        transform: scale(1.02);
    }

    .subject-title {
        color: #007bff;
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 20px;
        text-align: center;
    }

    .resource-link {
        color: #007bff;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
    }

    .resource-link:hover {
        color: #0056b3;
    }

    .sidebar .sidebar-content {
        background-color: #f1f1f1;
    }

    h3 {
        color: #343a40;
        margin-top: 20px;
    }

    p {
        color: #555;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        border: 1px solid #ddd;
    }

    .footer p {
        color: #555;
        font-size: 14px;
    }

    .whats-new {
        background-color: #e6f3ff;
        border-left: 5px solid #007bff;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
    }

    .whats-new h4 {
        color: #007bff;
        margin-top: 0;
    }

    .whats-new ul {
        margin-bottom: 0;
        padding-left: 20px;
        font-size: 15px;
    }

    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }

    @keyframes slideIn {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(0); }
    }

    .slideIn {
        animation: slideIn 1s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# "What's New" Section
st.markdown("""
<div class="whats-new fadeIn">
    <h4>What's New:</h4>
    <ul>
""" + "".join([f"<li>{item}</li>" for item in whats_new]) + """
    </ul>
</div>
""", unsafe_allow_html=True)

# Subjects Data
subjects = {
    "ECM": {
        "Tips and Tricks": """
            1. Go through the provided PPTs at least once and understand the key concepts.
            2. Solve and understand the concepts in assignments. If you're stuck, use resources like Chegg or Homeworkify, and refer to senior students' assignment papers.
            3. Solving previous year questions is crucial for midterms and final exams.
        """,
        "Lectures": "https://drive.google.com/drive/folders/1hx_Lpxzb6IGkDDFdIH8rt9t1IQRTHMxl",
        "Previous Year Question Papers": "https://drive.google.com/drive/u/0/folders/1egIbmKGoCK2E9nSzFUgxKH5c4As6xsoB",
        "Assignment Question Papers": "https://drive.google.com/drive/u/1/folders/1gL_f-HYC5NyN3DmBF309zu7dI-wLIFJm",
        "Importance Graph": {
            "labels": ["Solving Previous Year Papers", "Understanding Assignments", "Direct Class Questions"],
            "sizes": [50, 30, 20]
        }
    },
    "PCP": {
        "Tips and Tricks": """
            1. Focus on solving previous year question papers.
            2. Try to collect as many question papers as possible from 2017 or earlier.
            3. Remember that questions may not be directly repeated from the last year, so review papers from two years before as well.
        """,
        "Link for All Materials": "https://drive.google.com/drive/folders/1ke-PfLyyXR2CqFqbAyYVOQc4u9et76ab",
    },
}

st.sidebar.title("Subjects")
st_lottie(lottie_book, height=200, key="sidebar_animation")
selected_subject = st.sidebar.radio("Choose a subject", list(subjects.keys()))

st.markdown(f"<h1 class='subject-title fadeIn'>{selected_subject} Resources</h1>", unsafe_allow_html=True)

st_lottie(lottie_coding, height=300, key="main_animation")

st.markdown(f"<h3 class='slideIn'>Tips and Tricks:</h3><p>{subjects[selected_subject]['Tips and Tricks']}</p>", unsafe_allow_html=True)

if selected_subject == "ECM":
    st.markdown("<h3> Study Strategy:</h3>", unsafe_allow_html=True)
    labels = subjects["ECM"]["Importance Graph"]["labels"]
    sizes = subjects["ECM"]["Importance Graph"]["sizes"]
    
    df = pd.DataFrame({"Strategy": labels, "Importance": sizes})
    
    chart = alt.Chart(df).mark_arc().encode(
        theta=alt.Theta(field="Importance", type="quantitative"),
        color=alt.Color(field="Strategy", type="nominal"),
        tooltip=["Strategy", "Importance"]
    ).properties(width=400, height=400)
    
    st.altair_chart(chart, use_container_width=True)

for resource, link in subjects[selected_subject].items():
    if resource not in ["Tips and Tricks", "Importance Graph"]:
        st.markdown(f"""
        <div class='resource-card'>
            <a href='{link}' target='_blank' class='resource-link'>{resource}</a>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer fadeIn">
    <p>From senior to junior</p>
    <p>ALL THE BEST...</p>
</div>
""", unsafe_allow_html=True)
