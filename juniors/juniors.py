import streamlit as st
import matplotlib.pyplot as plt
import random

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
</style>
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
        "Link for All Materials": "https://drive.google.com/drive/folders/1ke-PfLyyXR2CqFqbAyYVOQc4u9et76ab"
    },
    "SWM": {
        "Tips and Tricks": """
            1. Prepare whatever sir gives.
            2. Obtain and study previous year question papers.
            3. Ensure to do every task they give.
        """,
        "Previous Year Question Papers": "https://drive.google.com/drive/folders/1kmKctDWKd1rU6RX6mJilvkawMybFR5B-",
        "Assignment Question Papers and Answer": "https://drive.google.com/drive/u/0/folders/1dfwMD7i6znx7uyACxhaaYDuUyFp8V3i0"
    },
    "EMDA": {
        "Tips and Tricks": """
            1. Focus on understanding everything from the provided PPTs, as questions are rarely asked from outside these materials.
        """,
        "Class lecture ppt": "https://drive.google.com/drive/u/1/folders/1VMQo7o4FjEqaUxBcBsTFARj3UxUZExaH"
    }
}


st.sidebar.title("Subjects")
selected_subject = st.sidebar.radio("Choose a subject", list(subjects.keys()))


st.markdown(f"<h1 class='subject-title'>{selected_subject} Resources</h1>", unsafe_allow_html=True)


st.markdown(f"<h3>Tips and Tricks:</h3><p>{subjects[selected_subject]['Tips and Tricks']}</p>", unsafe_allow_html=True)


if selected_subject == "ECM":
    st.markdown("<h3>Importance of Study Strategies:</h3>", unsafe_allow_html=True)
    labels = subjects["ECM"]["Importance Graph"]["labels"]
    sizes = subjects["ECM"]["Importance Graph"]["sizes"]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    st.pyplot(fig)


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

if st.button("Click here if you are bored!"):
    surprise = random.choice(effects)
    if surprise == 'balloons':
        st.balloons()
    elif surprise == 'snow':
        st.snow()
    elif surprise == 'custom_message':
        st.markdown(f"<h1 style='text-align: center;'>{random.choice(random_messages)}</h1>", unsafe_allow_html=True)


st.markdown("""
<div class="footer">
    <p>From senior to junior</p>
    <p>ALL THE BEST...</p>
</div>
""", unsafe_allow_html=True)
