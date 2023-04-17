import streamlit as st
from PIL import Image

# Custom CSS for Headings
st.markdown("""
<style>
    h1 {
        color: #0afa9e;
    }
    h2 {
        color: #0afa9e;
    }
</style>
""", unsafe_allow_html=True)

# Animated Background
st.markdown("""
<div style="background-color: #000; position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;">
    <canvas id="backgroundCanvas" style="width: 100%; height: 100%;"></canvas>
</div>
<script>
// Add your JavaScript code for the animation here.
</script>
""", unsafe_allow_html=True)

# Header
st.title('Lakshay Chawla - Data Scientist')

# Futuristic Image
header_image = Image.open('spacebottle.jpg')
st.image(header_image, width=700)

# Introduction
st.header("I'd rather use my superpowers to understand humans - a cloud mind.")

# Education
st.header('Education')
st.write("""
- Bachelor of Technology in Computer Science Engineering from Maharaja Agrasen Institute of Technology (2018-2022), 8.6 CGPA
- Grade 10 & Grade 12 from D.A.V. Public School, Sector-14, Faridabad (10 CGPA and 93.6% respectively)
""")

# Skills
st.header('Skills')
st.write("""
- Machine Learning
- Artificial Intelligence
- Data Science
- Python
- PySpark
- Hadoop
- Hive
""")

# Work Experience
st.header('Work Experience')
st.write("""
1. Teaching Assistant at Univ.AI (May 2022 - Present)
2. Big Data Analyst Intern at Appinventiv Technologies Pvt Ltd. (February 2022 - June 2022)
3. Big Data Analyst Intern at JIO PLATFORMS LIMITED (August 2021 - February 2022)
4. Big Data Analyst Intern at HAVELLS INDIA LIMITED (January 2021 - July 2021)
""")

# Projects
st.header('Projects')
st.write("""
1. Classifying Periodic Variable Stars
2. Music Genre Prediction
3. Customer Relationship Prediction
""")

# Publications
st.header('Publications')
st.write("""
- Machine Learning Model to Analyze Mental Health, published in ICICC (International Conference on Innovative Computing and Communication), February 2022.
""")

# Certificates
st.header('Certificates')
st.write("""
1. Master ML & AI program: Univ.AI [01/2022 - 07/2022]
2. Satellite based Navigation A Journey from GPS to Mobile Phone Platform: IIRS-ISRO [03/2021 - 03/2021]
3. Python for Data Science Essential Training Part 1 & 2: LinkedIn Learning [10/2021 - 10/2021]
4. Analyzing Big Data with Hive: LinkedIn Learning [10/2021 - 10/2021]
5. Python Essential Training: LinkedIn Learning [08/2021 - 08/2021]
6. Data Science and Machine Learning Course: Coding Ninjas [06/2019 - 02/2020""")

# Interests
st.header('Interests')
st.write("""
- Behavioural Economics
- Strategic Gaming
- Clinical Psychology
- Writing
- Music
- Traveling
""")

# Footer (Contact and Social Media Links)
st.write("""
### Contact
Email: lakshaychawla13@gmail.com

Phone: +91 9811096411

### Social Media
- [LinkedIn](https://www.linkedin.com/in/lakshaychawla13/)
- [GitHub](https://github.com/Lakshay-13)
""")
