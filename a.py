import streamlit as st
from PIL import Image
import time

# Page Configurations
st.set_page_config(page_title="Ramanprit Kaur | Portfolio", page_icon="🎯", layout="wide")

# Custom Styles
st.markdown(
    """
    <style>
        .main-title { text-align: center; font-size: 2.5em; color: #00ffcc; }
        .sub-title { text-align: center; font-size: 1.5em; color: #ffffff; }
        .section-title { font-size: 2em; color: #ffcc00; margin-top: 30px; }
        .contact-btn { background-color: #00ccff; color: white; padding: 10px; border-radius: 5px; }
        .profile-pic img { border-radius: 50%; display: block; margin-left: auto; margin-right: auto; }
    </style>
    """,
    unsafe_allow_html=True
)
with open("Profile.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

# Profile Section
col1, col2 = st.columns([1, 2])
with col1:
    image = Image.open("pc.jpg")  # Ensure you have a profile image
    st.image(image, width=400)
with col2:
    st.markdown("<p class='main-title'>Hi! I'm Ramanprit Kaur</p>", unsafe_allow_html=True)
    social_icons_data = {
    "LinkedIn": ["https://www.linkedin.com/in/ramanprit-kaur-1b856a2b6/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
    "GitHub": ["https://github.com/ramanprit07", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"]
    }

    social_icons_html = [
    f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
    f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
    f" style='width: 25px; height: 35px;'></a>"
    for platform in social_icons_data
]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>A passionate Data Analyst,Data Visualization & Machine Learning Enthusiast</p>", unsafe_allow_html=True)
    st.write(
        "I am a passionate Data Analyst with expertise in Python, SQL, and Machine Learning. "
    "I specialize in analyzing complex datasets, building predictive models, and creating insightful dashboards. "
    "With hands-on experience in Power BI, I transform raw data into actionable business intelligence." )
    
    # st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/ramanprit-kaur-1b856a2b6/) ", unsafe_allow_html=True)
    # st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-View-black)](https://github.com/ramanprit07)", unsafe_allow_html=True)
    st.download_button(label="📄 Download my Resume", data=pdf_bytes, file_name="Raman_resume.pdf", mime="application/pdf",)

# Projects Section
st.markdown("<h2 style='text-align: center; color: cyan;'> 📂 Projects </h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### AI Cyber Vanguard App")
    image_path1 = "ai.png" 
    st.image(image_path1, width=300)
    st.write("A cybersecurity app using machine learning to detect cyber threats, featuring phishing URL detection, ransomware detection, and password strength checking.")
    st.markdown("[View Project](https://mlcyber.streamlit.app/)")

with col2:
    st.markdown("### FitGenie - Nutrition Analysis")
    image_path1 = "fit2.png" 
    st.image(image_path1, width=300)
    st.write("A data science project that provides nutritional analysis and insights based on food images using Google Generative AI.")
    st.markdown("[View Project](https://nitrofit.streamlit.app/)")
col3, col4 = st.columns(2)

with col3:
    st.markdown("### Power BI - Sales Dashboard")
    image_path3 = "power bi.jpg"  # Replace with actual image path
    st.image(image_path3, width=300)
    st.write("A Power BI project analyzing total transactions, product details, and revenue to derive actionable insights.")
    # st.markdown("[View Dashboard](#)")  # Add actual link

with col4:
    st.markdown("### Billing Software")
    image_path4 = "bill.png"  # Replace with actual image path
    st.image(image_path4, width=300)
    st.write("A Python-based billing software with database integration to store and manage billing records efficiently.")
    # st.markdown("[View Project](#)")  # Add actual link




# Title with cyber theme
st.markdown("<h2 style='text-align: center; color: cyan;'>🚀 Skills</h2>", unsafe_allow_html=True)

# Define skills with corresponding image paths
skills = {
    "Python": "python.jpg",
    "Pandas": "pandas.jpg",
    "Plotly": "plotly.jpg",
    "NumPy": "numpy.jpg",
    "Matplotlib": "matplot.jpg",
    "Seaborn": "seaborn.jpg",
    "Streamlit": "streamli.png",
    "Jupyter Notebook": "jupy.jpeg",
    "Google Colab": "colab.png",
    "Excel": "excel.png",
    "SQL, PL/SQL, Apex Oracle": "sql.jpeg",
    "Power BI": "Power-BI.png"
}

# Define number of columns per row
num_cols = 5
cols = st.columns(num_cols)

# Display skills in a grid layout
for index, (skill, img) in enumerate(skills.items()):
    with cols[index % num_cols]:  # Distribute across columns
        st.image(img, caption=skill, width=100)

# Apply some CSS for better alignment and hover effect
st.markdown("""
    <style>
        .stImage img {
            border-radius: 12px;
            transition: transform 0.3s ease-in-out;
        }
        .stImage img:hover {
            transform: scale(1.1);
            box-shadow: 0px 4px 10px rgba(0, 255, 255, 0.6);
        }
    </style>
""", unsafe_allow_html=True)

import streamlit as st

# Title for Certification Section
st.markdown("<h2 style='text-align: center; color: cyan;'>🏆 Certifications</h2>", unsafe_allow_html=True)

# Certification data with titles and direct links
certifications = [
    ("Python & SQL - Net Max Technologies", "https://drive.google.com/file/d/1mV_Xeq180Ybb8tkcJP992NisRcpHFJdr/view?usp=drivesdk"),
    ("Cybersecurity - Net Max Technologies", "https://example.com/cert_cybersecurity.jpg"),
    ("Data Science & Machine Learning - O7 Services", "https://drive.google.com/file/d/1A0EaQ-gUeHsM2Ru5V-eVL9RuhOlFW1wW/view?usp=drivesdk"),
    ("The Brainiacs - Issued by IIC, DAV University", "https://drive.google.com/file/d/1vxug9LTKCXslx5umiOr4ithmwo5F93kE/view?usp=drivesdk"),
    ("Intro to Data Science - Cisco", "https://drive.google.com/file/d/1-kmKvWgk6oWqpFDaJwuqeAwDNWkAaYJd/view?usp=drivesdk")
]

# Define the number of columns per row
num_cols = 2
cols = st.columns(num_cols)

# Display certifications
for index, (title, link) in enumerate(certifications):
    with cols[index % num_cols]:  # Arrange in columns
        st.markdown(f"**{title}**")  # Display certificate title
        
        # Create a button-like clickable link
        st.markdown(
            f'<a href="{link}" target="_blank" style="text-decoration: none;">'
            f'<button style="background-color: #008CBA; color: white; border: none; padding: 8px 12px; '
            f'border-radius: 5px; cursor: pointer;">View Certificate</button></a>',
            unsafe_allow_html=True
        )






# Footer
st.markdown("---")
st.markdown("<p style='text-align:center'>🌟 Have A Wonderfull Day!!! 🌟</p>", unsafe_allow_html=True)
