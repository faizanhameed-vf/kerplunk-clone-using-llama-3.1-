import streamlit as st
import requests

# Input fields
jobTitle = st.text_input("Enter Job title")
jobCategory = st.text_input("Enter Job Category")
jobSubCategory = st.text_input("Enter Job Sub Category")

# Check if job description exists in session state
if "job_description" not in st.session_state:
    st.session_state.job_description = ""

if "questions" not in st.session_state:
    st.session_state.questions = ""

if "answers" not in st.session_state:
    st.session_state.answers = ""

# Function to generate the job description
def generateDescription():
    url_llama_chat = "http://127.0.0.1:8000/llama-chat/"
    data_llama_chat = {
        "prompt": f"""I am providing you job title, category, sub category. 
        You need to generate a job description accordingly. Job title: {jobTitle},
        Category: {jobCategory}, Sub-Category: {jobSubCategory}.
        Write in a descriptive tone that is ready to post.
        Do not use words like 'here is the project description.' Directly start with 'We are seeking...'
        """
    }
    
    # Make API request for job description
    response_llama_chat = requests.post(url_llama_chat, json=data_llama_chat)
    
    # Extract and store the job description in session state
    if response_llama_chat.status_code == 200:
        st.session_state.job_description = response_llama_chat.json().get("response", "")
        st.write(st.session_state.job_description)
    else:
        st.write("Error fetching job description.")

# Function to generate interview questions
def generateQuestions():
    if st.session_state.job_description:
        url_llama_chat_questions = "http://127.0.0.1:8000/llama-chat-questions"
        data_llama_chat_questions = {
            "prompt": f"""Generate 7 interview questions based on this job description:\n {st.session_state.job_description}.
            Ensure the questions assess the following abilities of the candidate
            1. Role Specific Capabilities (Asked through Technical Questions)
            2. Evaluation Notes (Conclusion, Pros, Cons, and things to follow up on)
            Leadership skills
            Communication Skills
            Attitude Towards Job
            Maturity
            Ability to get along with team
            Logical Thought process
            IQ Level
            Personality
            Technical Rating
            Provide only the questions, without any additional explanation or references. Ready to post."""
        }
        
        # Make API request for interview questions
        response_llama_chat_questions = requests.post(url_llama_chat_questions, json=data_llama_chat_questions)
        
        # Store generated questions in session state
        st.session_state.questions = response_llama_chat_questions.json().get("response", "")
        st.write("# Generated Interview Questions:")
        st.write(st.session_state.questions)

# Function to generate review based on answers
def generateReview():
    url_llama_review = "http://127.0.0.1:8000/llama-chat-review"
    data_llama_review = {
        "prompt": f"""Generate Review based on answers: \n{st.session_state.answers} 
        to these questions:\n {st.session_state.questions}\n.
        Write a short paragraph for each about the candidate's 
        Role Specific Capabilities (Asked through Technical Questions),
        Evaluation Notes (Conclusion, Pros, Cons, and things to follow up on),
        and Personality.
        
        Rate the following 7 attributes on a scale of poor, fair, average, good, or excellent:
        Leadership skills, Communication Skills, Attitude Towards Job, Maturity, 
        Ability to get along with team, Logical Thought process, IQ Level.
        
        Provide the candidate's Technical Rating from the following options:
        1- Absolute Rejection
        2- Can try some time later
        3- Average Exposure - Average Experience
        4- Average Exposure - Very good in the tech we need
        5- Average Potential - Limited exposure or can be tried on other things
        6- Good potential - Good foundation but no exposure
        7- Good potential - Good foundation and limited exposure
        8- Good potential - Good foundation and experience
        9- Excellent potential - Exceeds job expectations
        10- Absolute Guru

        """
    }
    
    response_llama_review = requests.post(url_llama_review, json=data_llama_review)
    job_review = response_llama_review.json().get("response", "")
    st.write(job_review)

# Only call the API for job description when all fields are filled
if jobTitle and jobCategory and jobSubCategory:
    # Button to generate job description
    if st.button("Generate Job Description"):
        generateDescription()

    # Button to generate interview questions (only if job description is present)
    if st.session_state.job_description:
        if st.button("Generate Interview Questions"):
            generateQuestions()

    # Display text area for answers and process the review
    if st.session_state.questions:
        st.session_state.answers = st.text_area("Enter Answers here", height=200)
        
        if st.button("Submit Answers and Generate Review"):
            generateReview()

else:
    st.write(" ")
