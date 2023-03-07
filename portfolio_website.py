import pandas
import streamlit as st


#creating page configuration
st.set_page_config(layout="wide")

#creating two columns for the page
col_1 ,col_2= st.columns(2)

#opening the col1 with context manager
with col_1 :
    #adding image
    st.image("App Images/alp.jpg")

# opening the col_2 with context manager
with col_2:
    # adding Title
    st.title("Athira Lakshmi Prakash")
    # adding details
    Professional_summary_content="""Hello, I am Athira ,a passionate software developer with a focus on Python and  Permanent Resident of Canada .I have B.Tech in Electrical Engineering and i have worked in Electrical field for the past 3 years.As an experienced Electrical Engineer, I am excited to have transitioned my skills and knowledge to the field of software development. I have a strong passion for learning new skills.
I love building Apps from the scratch , adding features to another apps and fixing bugs.My primary interest lies in full stack development ,Data Science, Artificial Intelligence, Internet of things(IoT), Machine Learning etc. Looking forward to work with exciting projects. I am confident that my skills and knowledge in Python combined with industry relevant soft skills will be a valuable asset to any organization.."""
    #adding content with background colour text box
    st.info(Professional_summary_content)

#adding a note
content="Have a look at cool Apps i built in Python . Feel free to contact me for your feedback , suggestion and collaboration"
st.write(content)

#adding two columns for the projects, description,image and source code
col_3,col_4= st.columns(2)

#creating a data frame using pandas to extract "title","description',"image etc
df=pandas.read_csv("data.csv",sep=";")

#print(df)


## opening the col_3 with context manager
with col_3:
    #extracting the details from data.csv files by converting that to a data frame.
    #iterating through the rows of df
    for index,row in df[:10].iterrows():
        #extracting title and writing it on webapp
        st.header(row["title"])
        st.write(row["description"])
        #image method to add image
        st.image("App Images/"+row['image'])
        #  link is wrote in()along with text in [] . eg. [click here](www.python.com)
        text = "Source Code"
        link = row["url"]
        st.markdown(f"[{text}]({link})", unsafe_allow_html=True)

## opening the col_4 with context manager
with col_4:
    for index,row in df[10:].iterrows():
        #extracting title and writing it on webapp
        st.header(row["title"])
        st.write(row["description"])
        st.image("App Images/" + row['image'])
        #  link is wrote in()along with text in [] . eg. [click here](www.python.com)
        text="Source Code"
        link=row["url"]
        st.markdown(f"[{text}]({link})", unsafe_allow_html=True)






