# Import the Necessary Libraries
import streamlit as st
import time
import numpy as np
import pandas as pd
from model import ensemble
from database import *


#calling the create_table function
@st.cache_resource
def call_create_table():
    try:
        create_table()
    except:
        print("Error in creating the table")


call_create_table()


def take_input():
    # This code is used to create two text inputs, one for a name and the other for an email address.
    # The name input is mandatory and the email must be at least 5 characters long.
    # If either of these conditions are not met, an error message is displayed.

    name = st.text_input(":violet[Name] :red[*]", key='4')
    email = st.text_input(":violet[Email] :red[*]", key='5')
    if (len(name) == 0) and len(email) < 5:
        st.error("Name and Email Input cannot be empty")

# This code is used to take in a list of seven numbers or eight for other course from a user
# Check if the values are within a range of 0 and 100.
# If the values are within range, the code will take the average of the seven or eight numbers
# It will the add the sum to the empty list  'var'.
# If the values are not within range, an error message will appear.
# If the user does not input seven numbers or eight for other courses , an error message will appear.

    var = []
    software = st.text_input(":blue[System Software] :violet[(com210,com221,com223,com310,com315,com211,com326)]:red[*]", key='0')
    new = software.split(",")
    if len(new) == 7:
        if (int(min(new)) >= 0) and (int(max(new)) <= 100):
            y = 0
            for i in new:
                y = (y + int(i))
            y = y / len(new)
            var.append(y)
        else:
            st.error("Value must be in range 0 and 100")
    else:
        st.error("Inconsistent number of input")

    elect = st.text_input(":blue[Digital Electronics] :violet[(com212,com225,com217,com310,com314,com320,mat210)]:red[*]", key='1')
    new1 = elect.split(",")
    if len(new1) == 7:
        if (int(min(new1)) >= 0) and (int(max(new1)) <= 100):
            y1 = 0
            for j in new1:
                y1 = (y1 + int(j))
            y1 = y1 / len(new1)
            var.append(y1)
        else:
            st.error("Value must be in range 0 and 100")
    else:
        st.error("Inconsistent number of input")

    soft = st.text_input(":blue[Software Engineering] :violet[(com220,com312,com315,com318,com321,com323,com324,com326)]:red[*]", key='2')
    new2 = soft.split(",")
    if len(new2) == 8:
        if (int(min(new2)) >= 0) and (int(max(new2)) <= 100):
            y2 = 0
            for j in new2:
                y2 = (y2 + int(j))
            y2 = y2 / len(new2)
            var.append(y2)
        else:
            st.error("Value must be in range 0 and 100")
    else:
        st.error("Inconsistent number of inputs")

    network = st.text_input(":blue[Networking] :violet[(mat212,mat220,com224,com315,com318,com319,com322,com323)]:red[*]", key='3')
    new3 = network.split(",")
    if len(new3) == 8:
        if (int(min(new3)) >= 0) and (int(max(new3)) <= 100):
            y3 = 0
            for j in new3:
                y3 = (y3 + int(j))
            y3 = y3 / len(new3)
            var.append(y3)
        else:
            st.error("Value must be in range 0 and 100")
    else:
        st.error("Inconsistent number of input")

    # This code creates a NumPy array from the variable 'var', reshapes it to a 1-dimensional array.
    # Then creates a button which will call the predict function when clicked.
    # The predict function takes the reshaped array as an argument and returns the prediction of the ensemble model.
    # A success message is later displayed to the screen
    var = np.array(var)
    var = var.reshape(1, -1)

    if st.button("Predict"):
        @st.cache_resource
        def predict(data):
            pred = ensemble.predict(data)
            pred = pred.reshape(-1, 1)
            return pred

        pred = predict(var)
        with st.spinner("Predicting..."):
            time.sleep(3)
        st.success("Prediction Done", icon="✅")

        # st.cache_data is a decorator that can be used to cache the output of a function.
        '''When the function is called again with the same arguments, \
        the cached value is returned instead of executing the function.'''

        @st.cache_data
        def check(pred):
            if pred == 1:
                category = 'Digital Electronics'
            elif pred == 2:
                category = 'System Software'
            elif pred == 3:
                category = 'Software Engineering'
            else:
                category = 'Networking'
            return category

        prediction = check(pred)

        # This code checks if the email provided by the user already exists in the database.
        # If it does, it will display an error message.
        '''Otherwise, it will create a dataframe of people doing the same project as the user \
        # and add the user's name, email, and project to the database and display the dataframe of people\
        doing the same project as the user.'''

        name1 = check_mail(email)
        if email in str(name1).strip("[]()'',"):
            st.error("email Already Exist..")
        else:
            pass
        # st.dataframe(view_all_data())
        peers = select_user(prediction)

        df = pd.DataFrame(peers, columns=["Name", "Email"])
        st.info("People doing **{}** project like you include :".format(prediction))
        add_userdata(name, email, prediction)
        st.write(df)



