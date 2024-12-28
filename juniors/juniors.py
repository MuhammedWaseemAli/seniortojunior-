import streamlit as st
import matplotlib.pyplot as plt
import random
import pandas as pd
import altair as alt
from streamlit_lottie import st_lottie
import requests

# Data Structures
whats_new = [
    {"update": "Updated Madhav sir lecture in PCP", "date": "2024-12-28"},
    {"update": "Added PCP textbooks (Peavy and Benefield)", "date": "2024-12-27"},
    {"update": "Added EMDA question papers", "date": "2024-12-26"},
    {"update": "Added SWM textbooks and PPT", "date": "2024-12-25"},
    {"update": "Added PCP 2019 question paper in quiz folder", "date": "2024-12-24"}
]

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

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
lottie_animations = {
    "book": load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1a8dx7zj.json"),
    "coding": load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json"),
    "study": load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_vvx2gjpt.json"),
    "rocket": load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_myejiggj.json"),
    "success": load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_xnh1jp0k.json")
}

# Fun facts
fun_facts = [
    "Did you know? Taking short breaks during study sessions can improve retention by up to 20%!",
    "The best time to review your notes is within 24 hours of taking them.",
    "Studies show that teaching others can improve your own understanding by up to 90%!",
    "Regular exercise can boost your memory and thinking skills!",
    "Music can help you study better, especially Mozart's compositions!"
]

# Page configuration
st.set_page_config(
    page_title="Educational Resources Dashboard",
    page_icon="📚",
    layout="wide"
)

# Hide Streamlit default elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #007BFF, #00C6FF);
        color: white;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 123, 255, 0.2);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 123, 255, 0.3);
    }
    
    .resource-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .resource-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
    }
    
    .subject-title {
        background: linear-gradient(45deg, #007BFF, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem 0;
    }
    
    .whats-new {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        border-left: 5px solid #007BFF;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    .update-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid #eee;
    }
    
    .update-date {
        color: #666;
        font-size: 0.9rem;
    }
    
    .fun-fact-card {
        background: linear-gradient(45deg, #FF512F, #F09819);
        color: white;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(255, 81, 47, 0.2);
    }
    
    .tooltip {
        position: relative;
        display: inline-block;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 5px 10px;
        border-radius: 6px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    .resource-link {
        text-decoration: none;
        color: #007BFF;
        transition: color 0.3s ease;
    }
    
    .resource-link:hover {
        color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Enhanced header with animation
st.markdown("<h1 class='subject-title'>Educational Resources Dashboard</h1>", unsafe_allow_html=True)
st_lottie(lottie_animations["rocket"], height=200)

# Enhanced What's New section
st.markdown("""
<div class="whats-new">
    <h3>📢 Latest Updates</h3>
""", unsafe_allow_html=True)

for update in whats_new:
    st.markdown(f"""
    <div class="update-item">
        <span>{update['update']}</span>
        <span class="update-date">{update['date']}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Enhanced sidebar
st.sidebar.title("📚 Subject Navigator")
st_lottie(lottie_animations["book"], height=150, key="sidebar_animation")
selected_subject = st.sidebar.radio("Choose your subject", list(subjects.keys()))

# Main content
st.markdown(f"<h1 class='subject-title'>{selected_subject} Resources</h1>", unsafe_allow_html=True)
st_lottie(lottie_animations["study"], height=200)

# Enhanced Tips and Tricks section
st.markdown("""
<div class="resource-card">
    <h3>🎯 Tips and Tricks</h3>
""", unsafe_allow_html=True)
st.markdown(subjects[selected_subject]['Tips and Tricks'])
st.markdown("</div>", unsafe_allow_html=True)

# Display importance graph for ECM
if selected_subject == "ECM":
    st.markdown("<h3>📊 Study Strategy Breakdown</h3>", unsafe_allow_html=True)
    data = pd.DataFrame({
        'Strategy': subjects['ECM']['Importance Graph']['labels'],
        'Percentage': subjects['ECM']['Importance Graph']['sizes']
    })
    
    chart = alt.Chart(data).mark_arc().encode(
        theta=alt.Theta(field="Percentage", type="quantitative"),
        color=alt.Color(field="Strategy", type="nominal"),
        tooltip=['Strategy', 'Percentage']
    ).properties(width=400, height=400)
    
    st.altair_chart(chart, use_container_width=True)

# Enhanced resource cards
for resource, link in subjects[selected_subject].items():
    if resource not in ["Tips and Tricks", "Importance Graph"]:
        st.markdown(f"""
        <div class="resource-card">
            <div class="tooltip">
                <a href="{link}" target="_blank" class="resource-link">
                    <h4>📑 {resource}</h4>
                </a>
                <span class="tooltiptext">Click to open resource</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Random fun fact
st.markdown("""
<div class="fun-fact-card">
    <h3>💡 Did You Know?</h3>
""", unsafe_allow_html=True)
st.write(random.choice(fun_facts))
st.markdown("</div>", unsafe_allow_html=True)

# Enhanced motivation button
if st.button("🎉 Need Some Motivation?", key="motivation_button"):
    st_lottie(lottie_animations["success"], height=200)
    st.markdown(f"""
    <div class="resource-card">
        <h3>🌟 {random.choice(random_messages)}</h3>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="resource-card" style="text-align: center;">
    <h3>From Senior to Junior""")
