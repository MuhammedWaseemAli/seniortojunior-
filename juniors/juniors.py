import streamlit as st
import matplotlib.pyplot as plt
import random
import pandas as pd
import altair as alt
from streamlit_lottie import st_lottie
import requests

whats_new = [
    "updated madhav sir lecture in pcp. dont spend time on it more at beginning . it will be useful at end when he teaches advance topics . ",
    "updated pcp text books which he refer peavy and benefield",
    "EMDA question papers",
    "SWM textbooks and ppt"
    # Add more items as you make changes
]


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_book = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json")
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")


st.markdown("""
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
        color: #333;
    }

    .main {
        padding: 20px;
    }

    .stButton>button {
        color: #ffffff;
        background-color: #007BFF;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 14px;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #0056b3;
    }

    .resource-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        border: 1px solid #ddd;
        transition: transform 0.3s ease-in-out;
    }

    .resource-card:hover {
        transform: scale(1.05);
    }

    .subject-title {
        color: #333;
        font-size: 36px;
        font-weight: 600;
        margin-bottom: 20px;
        text-align: center;
    }

    .resource-link {
        color: #007BFF;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
    }

    .resource-link:hover {
        color: #0056b3;
    }

    .sidebar .sidebar-content {
        background-color: #f7f7f7;
    }

    h3 {
        color: #333;
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
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        border: 1px solid #ddd;
    }

    .footer p {
        color: #555;
        font-size: 14px;
    }

    .whats-new {
        background-color: #e6f3ff;
        border-left: 5px solid #007BFF;
        padding: 10px;
        margin-bottom: 20px;
        border-radius: 5px;
    }

    .whats-new h4 {
        color: #007BFF;
        margin-top: 0;
    }

    .whats-new ul {
        margin-bottom: 0;
        padding-left: 20px;
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

st.markdown("""
<div class="whats-new fadeIn">
    <h4>What's New:</h4>
    <ul>
""" + "".join([f"<li>{item}</li>" for item in whats_new]) + """
    </ul>
</div>
""", unsafe_allow_html=True)

subjects = {
    "ECM": {
        "Tips and Tricks": """
            1. Go through the provided PPTs at least once and understand the key concepts.
            2. Solve and understand the concepts in assignments. If you're stuck, use resources like Chegg or Homeworkify, and refer to senior students' assignment papers.
            3. Solving previous year questions is crucial for midterms and final exams.**please use your smail to access the contents below** ..
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
            4. Be prepared for some GATE-level questions that may be asked from IIT sources.
        """,
        "Link for All Materials": "https://drive.google.com/drive/folders/1ke-PfLyyXR2CqFqbAyYVOQc4u9et76ab",
        "Link for sir class": "https://drive.google.com/drive/u/0/folders/1bBR17lIAc7ZKQ3zet2JUMeBGZYgfOlT1",
        "Link for textbook sir refer": "https://drive.google.com/drive/u/0/folders/1ZlDnC7nXY7_eCb4PMIP8u1sHZ6AlND_d"
    },
    "SWM": {
        "Tips and Tricks": """
            1. Prepare whatever sir gives.
            2. Obtain and study previous year question papers.
            3. Ensure to do every task they give.
        """,
        "Previous Year Question Papers": "https://drive.google.com/drive/folders/1kmKctDWKd1rU6RX6mJilvkawMybFR5B-",
        "Assignment Question Papers and Answer": "https://drive.google.com/drive/u/0/folders/1dfwMD7i6znx7uyACxhaaYDuUyFp8V3i0",
        "text books and ppt ": "https://drive.google.com/drive/u/0/folders/10N6NVPHn4t533gmEqcZyt9KdAOfCDvfV"
    },
    "EMDA": {
        "Tips and Tricks": """
            1. Focus on understanding everything from the provided PPTs, as questions are rarely asked from outside these materials.
        """,
        "Class lecture ppt": "https://drive.google.com/drive/u/1/folders/1VMQo7o4FjEqaUxBcBsTFARj3UxUZExaH",
        "PREVIOUS QUESTION PAPER": "https://drive.google.com/drive/u/0/folders/1AqeGE8VslYlgm2LhuSj_BsIwXTZKNAe-"
    }
}


st.sidebar.title("Subjects")
st_lottie(lottie_book, height=200, key="sidebar_animation")
selected_subject = st.sidebar.radio("Choose a subject", list(subjects.keys()))


st.markdown(f"<h1 class='subject-title fadeIn'>{selected_subject} Resources</h1>", unsafe_allow_html=True)


st_lottie(lottie_coding, height=300, key="main_animation")


st.markdown(f"<h3 class='slideIn'>Tips and Tricks:</h3><p>{subjects[selected_subject]['Tips and Tricks']}</p>", unsafe_allow_html=True)


if selected_subject == "ECM":
    st.markdown("<h3>Importance of Study Strategies:</h3>", unsafe_allow_html=True)
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


effects = ['balloons', 'snow', 'custom_message']

random_messages = [
    "🎉 You are doing great! 🎉",
    "Do you know Ligy ma'am gives a lot of marks, more than we deserve if our approach is right.",
    "Madhav sir gives good grades. So don't worry. If he feels you work hard, he will give marks.",
    "Ligy ma'am likes to joke.",
    "If you have doubt regarding GATE and PSU, contact your senior Aditya. FACT: He even taught SSC JE for others.",
    "Bro you are so chill. So why worry :)",
    "Oh exams are nearby. Just be chill and study. I know you are nervous, but you got it bro! You reached up to here, so you can do it.",
    "oh you have placement related doubt ask mihir shinjini",
    "oh you need some study tips ask sreenivasulu ",
    "oh u wanna challenge someone in cricket challenge kartick",
    "oh you want chill person talk to korus the KOKO",
]

if st.button("Click here if you are bored!", key="surprise_button"):
    surprise = random.choice(effects)
    if surprise == 'balloons':
        st.balloons()
    elif surprise == 'snow':
        st.snow()
    elif surprise == 'custom_message':
        st.markdown(f"<h1 style='text-align: center;' class='fadeIn'>{random.choice(random_messages)}</h1>", unsafe_allow_html=True)


st.markdown("""
<div class="footer fadeIn">
    <p>From senior to junior</p>
    <p>ALL THE BEST...</p>
</div>
""", unsafe_allow_html=True)
