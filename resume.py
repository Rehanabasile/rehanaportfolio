import streamlit as st

# Set page layout and add styling
st.set_page_config(
    page_title="Portfolio - REHANA M",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add CSS styling for sidebar and profile image
st.markdown(
    """
    <style>
    .sidebar {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Header with colorful text
st.title(" REHANA M")
st.markdown("<h2 style='color: #FF5733;'>Data Analyst | Data Visualization Expert</h2>", unsafe_allow_html=True)


# ... Continue with the rest of the code ...
# Objective
st.header("Objective")
st.write("Data analyst experienced in Python, Excel, Looker, SQL, and C language. Proficient in data visualization and analysis. Seeking to contribute analytical skills and project expertise to data-driven decision-making.")
# Skills
st.header("Skills")
Skills = """
    - Programming: Python, C, Java (Basics).
    - Data Visualization: Excel ,Looker.
    - Databases: SQL (Basics).
    - Data Analysis: Exploratory Data Analysis (EDA), Statistical Analysis.
    - Projects: Sales Analysis Dashboard, Salary Prediction Web App, Portfolio Website.
    - Communication: Strong written and verbal skills.
"""
st.write(Skills)

# Education
st.header("Education")
st.write("Master of Physics")
st.write("St. Joseph’s College of Arts and Science")
st.write("April 2023")

# Projects
st.header("Projects")
projects = [
    "Sales Analysis Dashboard",
    "Salary Prediction Web App",
    "Portfolio Website",
    "Daily Expense Tracker Web App"
]
for i, project in enumerate(projects, start=1):
    st.write(f"{i}. {project}")

# Experience
st.header("Experience")
experience_text = """
Virtual Internship - [TATA]
[15.04.2023-17.07.2023]
- Collaborated to gather, clean, and validate data.
- Used Excel and Looker for interactive dashboards.
- Assisted in SQL data retrieval.
"""
st.write(experience_text)

# Certifications
st.header("Certifications")
certifications = """
   - DA Certification, Data Analyst Google.
   - Completed Project Management Certification.
   - Data Visualization Certificate at TATA Internship.
"""
st.write(certifications)

# Languages
st.header("Languages")
st.write("- English (Fluent)")

# References
st.header("References")
st.write("Available upon request.")


# Contact Information with animations
st.sidebar.header("Contact Information")
st.sidebar.write("Email: rehana2000jd@gmail.com")
st.sidebar.write("Phone: 9655936501")
st.sidebar.markdown("LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/rehana-rehana-46a9a3202/)")
st.sidebar.write("Follow me on social media!")


# Link to projects
st.sidebar.header("My Projects")
st.sidebar.markdown("[Salary Prediction Web App](https://salary-gwcp67mbbfc4rmzcxqc3kg.streamlit.app/)")
st.sidebar.markdown("[Daily Expense Tracker Web App](https://expense-tracker-ctx8bftnlt6gb39zmn3fgg.streamlit.app/)")

# Footer with thank you message and animation
st.markdown("<h3 style='color: #FF5733; text-align: center;'>Thank you for visiting my portfolio!</h3>", unsafe_allow_html=True)
st.sidebar.write("Stay tuned for more updates!")

# Add more styling, animations, and interactivity as desired

