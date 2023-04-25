import streamlit as st
# This code sets the configuration for a Streamlit page
st.set_page_config(page_title="Student Project Recommender", page_icon=":books:", layout="wide", initial_sidebar_state="auto")

from inputs import take_input


# It also hides the footer
st.markdown("<style>footer{display:none;}</style>", unsafe_allow_html=True)


# Creates a heading in HTML and CSS AND Display it using the streamlit Library

st.markdown('<p class="font">Project Recommender</p>', unsafe_allow_html=True)
st.markdown("""<style> .font
    { font-size:55px ; font-family:'Cooper Black'; color:#FF9633;
    }</style>""", unsafe_allow_html=True)

# This code modifies the font style of a markdown element
st.markdown("""<style> .font1
                        { font-size:40px ; font-family:'Open Sans', fantasy; color:#00A8E8;
                        }</style>""", unsafe_allow_html=True)


# This code creates a sidebar menu with two options, "Predict" and "About".
# The user can select one of the options and it is stored in the variable "choice".
menu = ["Predict", "About"]
choice = st.sidebar.selectbox("Menu", menu)



# This code creates two sections in the sidebar of the Streamlit app.
st.sidebar.title("Contributions")
st.sidebar.info(
    """
    This is an Open Source project and you are Welcomed to make any impactfull additions whatsoever.

    [GitHub Account](https://github.com/jomoziqu) | [Source code](https://github.com/jomoziqu/project-recommender)
    """
)

st.sidebar.title("Contact Developer")
st.sidebar.info(
    """
    **Wilson Jomo**: 

    [GitHub](https://github.com/jomoziqu) | [Medium](https://medium.com/@wilyjomo4495) | [LinkedIn](https://www.linkedin.com/in/wilson-jomo-a6179b25a)
    """
)


def predict_page():
    st.markdown('<p class="font1">Prediction Page</p>', unsafe_allow_html=True)
    st.write("Welcome to the Recommender Page. Here, you provide your input of the Courses Units \
    as indicated on the input box for Years 2 and 3.")
    st.info("Please provide your username and Email before continuing..")
    take_input()


# The above code is a function that creates an about page for a project recommender system.
# It displays text that provides information about the project, as well as links to the project's social media accounts.

def about_page():
    st.markdown('<p class="font1">About Page</p>', unsafe_allow_html=True)

    st.markdown("""
            <div style="background-color:#F0F8FF;padding 10px; font-family:sans-serif; font-size:16px;>"
            <p>We are a team of students from Rongo University, working on a project recommender system. Our goal is to help students
            find the best projects to work on, based on their past Academic Perfomance. We use data from students academic perfomance to 
            make our recommendations<p><b>Follow us on social media for updates and more information about this project</b></p></p>
            <ul>
            <li><a href="https:www.facebook.com/projectrecommender">Facebook</a></li>
            <li><a href="https://medium.com/@wilyjomo4495">Medium</a></li>
            <li><a href="https:www.twitter.com/projectrecommender">Twitter</a></li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


# This code checks the value of the variable "choice" and takes an action accordingly.
# If the value is "About", it calls the function about_page(), otherwise it calls the function predict_page()

if choice == 'About':
    about_page()

else:
    predict_page()
