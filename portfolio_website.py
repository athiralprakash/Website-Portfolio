import streamlit as st

#creating page configuration
st.set_page_config(layout="wide")

#creating two columns for the page
col_1 ,col_2= st.columns(2)

#opening the col1 with context manager
with col_1 :
    #adding image
    st.image("App Images/alp.jpg")

# opening the col1 with context manager
with col_2:
    # adding Title
    st.title("Athira Lakshmi Prakash")
    # adding details
    Professional_summary_content="""Hello, I am a passionate software developer with a focus on Python and  Permanent Resident of Canada .As an experienced Electrical Engineer, I am excited to have transitioned my skills and knowledge to the field of software development. I have a strong passion for learning new skills.
My primary interest lies in full stack development ,Data Science, Artificial Intelligence, Internet of things(IoT), Machine Learning etc. Looking forward to work with exciting projects. I am confident that my skills and knowledge in Python combined with industry relevant soft skills will be a valuable asset to any organization.
Below are the projects i have done in Python ."""
    #adding content with background colour text box
    st.info(Professional_summary_content)



