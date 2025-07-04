#An entry form for workers 
import streamlit as st
st.title("Good morning! welcome to the company")
st.write("Fill the below information to enter in the office and mark your attendence")
#to enter their name
with st.form("office_form"):
    name=st.text_input("Enter your name")
#to choose job occupation 
    options=["AI developer","Data Scientist","Data analyst","it expert","front_end developer","backend developer"]
    choice=st.selectbox("choose your job type:",options)
#to choose the time
    time=st.slider("Select the time",6,10)
#to submit the form
    submitted = st.form_submit_button("Submit")
#after submission
if submitted:
        if name:
            st.write(f"Welcome to the office, {name}! Have a great day and focus on your work. Thanks!")
        if choice:
            st.write(f"You have selected: {choice}")
        if time:
            if time <= 8:
                st.write(f"{name}, Good job! You arrived on time. You can enter the office.")
            elif time <= 9:
                st.write("Acceptable, but please try to arrive on time. You may now enter the office.")
        else:
            st.warning("you can go back to home and come on time tomorrow ")
        st.write("thanks for filling the information")
    #type streamlit run entry.py in terminal
