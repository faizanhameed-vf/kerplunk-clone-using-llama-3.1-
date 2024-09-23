import requests

url_llama_chat = "http://127.0.0.1:8000/llama-chat/"
data_llama_chat = {
    "prompt": """I am providing you job title, category, sub category, 
    you need to generate job description accordingly, job title : junior Frontend web Developer,
    Category : Software Engineer, Sub-Category : Frontend
    Write in descriptive tone that ready to post.
    Dont use words "here is the project description, Directly Start from , we are seeking for...."
    """
}

response_llama_chat = requests.post(url_llama_chat, json=data_llama_chat)


job_description = response_llama_chat.json().get("response", "")        
print(job_description)
#%%
url_llama_chat_questions = "http://127.0.0.1:8000/llama-chat-questions"

data_llama_chat_questions = {
            "prompt": f"""Generate 7 interview questions based on this job description:\n {job_description}.
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

response_llama_chat_questions = requests.post(url_llama_chat_questions, json=data_llama_chat_questions)
print(response_llama_chat_questions)
questions = response_llama_chat_questions.json().get("response", "")
print("Generated Interview Questions:")
print(questions)

#%%
answers = """Here’s a sample response to each of the interview questions:

1. **Can you explain a situation where you had to write clean and efficient front-end code using modern web technologies like HTML5, CSS3, JavaScript (ES6+), and React? How did you ensure that your code was well-documented?**

In a recent project, I was tasked with developing a dynamic dashboard using React and ES6+. My focus was on writing modular and reusable components, which ensured efficiency and reduced redundancy. I made extensive use of arrow functions, async/await for better readability, and CSS Flexbox for layout structuring. I followed best practices like using descriptive variable names, commenting on complex logic, and maintaining a separate documentation file that outlined the code structure and functionality. This made it easier for the team to understand and maintain the project over time.

2. **A designer has provided you with a visual design for a new feature, but it doesn't meet the technical requirements of our team. How would you communicate this to the designer and what approach would you take to resolve the issue?**

I would schedule a quick meeting with the designer to discuss the constraints of the design. My approach would be to explain the technical limitations clearly, for example, if certain animations would affect performance or if layout elements were not responsive. I would propose alternative solutions that meet the design's intent but fit within the project's technical boundaries. The goal would be to collaborate effectively while maintaining respect for both design and technical perspectives.

3. **If you were given a front-end project that had a critical bug, how would you troubleshoot and debug the issue? What tools or techniques would you use to identify and fix the problem?**

I typically begin by reproducing the bug in different environments to isolate the issue. I use Chrome DevTools to inspect the DOM and network requests to see if there are errors in the console or unexpected behaviors in the application flow. I also rely on breakpoints and logs to pinpoint where the code is failing. Once identified, I analyze the problem in the code, using techniques such as binary search to narrow down the cause. After fixing the bug, I test it extensively to ensure it doesn't cause regressions.

4. **Can you describe your experience with responsive design principles and mobile-first approaches? How do you ensure that your designs are accessible across different devices and browsers?**

I prioritize mobile-first development by starting with the smallest viewport size and progressively enhancing the design for larger screens. I use responsive units like `em`, `rem`, and percentages to ensure flexibility, and CSS media queries to adjust the layout for different screen sizes. To maintain consistency across browsers, I test extensively using tools like BrowserStack or cross-browser testing environments. Additionally, I focus on accessibility by implementing semantic HTML and following ARIA guidelines to ensure that the app is usable by people with disabilities.

5. **Suppose you were working on a team project and encountered a disagreement with a colleague about the best approach to take. How would you handle this situation and what communication skills would you use to resolve the issue?**

In such cases, I prefer an open and respectful discussion to understand both perspectives. I would ask my colleague to explain their approach and the rationale behind it while also presenting my point of view. If a consensus cannot be reached, I suggest running a quick test or prototype of both solutions to see which one performs better in practice. Effective communication, active listening, and staying solution-oriented are key in resolving such disagreements while maintaining a collaborative environment.

6. **Can you walk me through your process for staying up-to-date with the latest trends, tools, and technologies in frontend development? What resources do you use to learn new things and how often do you attend conferences or workshops?**

I stay up-to-date through a combination of online resources like blogs, YouTube channels, and newsletters (e.g., Smashing Magazine, CSS Tricks, and Dev.to). I also follow communities on GitHub and Twitter to stay informed about new libraries or frameworks. I dedicate time each week to experiment with new tools or technologies in side projects. While I don’t attend conferences frequently, I do participate in virtual meetups and workshops whenever possible to expand my network and learn from industry leaders.

7. **Imagine that you have been tasked with implementing a state management library (e.g., Redux) into an existing front-end project. How would you approach this task and what steps would you take to ensure that the implementation is successful?**

I would first assess the current state management strategy in the application and identify the components that could benefit from Redux. Next, I would plan out the Redux architecture—defining actions, reducers, and the state shape. My goal would be to integrate Redux incrementally to avoid breaking changes and ensure backward compatibility. After the initial setup, I would test thoroughly to ensure state transitions work as expected. I’d also update documentation and provide the team with guidelines on how to use Redux effectively in the project going forward.
"""

url_llama_review = "http://127.0.0.1:8000/llama-chat-review"

data_llama_review = {
            "prompt": f"""Generate Review bases on answers to these questions questions:\n {questions}\n 
            answers: \n{answers}. Write a short paragraph for each about candidate's 
            Role Specific Capabilities (Asked through Technical Questions)
            Evaluation Notes (Conclusion, Pros, Cons, and things to follow up on)
            Personality.
            
            Rate the following attributes to poor,fair,average,good,excellent
            Leadership skills
            Communication Skills
            Attitude Towards Job
            Maturity
            Ability to get along with team
            Logical Thought process
            IQ Level.
            
            Tel me how uou rate candidate's Technical Rating Final *
            1- Absolute Rejection
            2-Can try Some time later
            3-Average Exposure- Average Experience
            4-Average Exposure- But very good in the tech we need
            5-Average Potential- Limited exposure or can be tried on other things
            6-Good potential- Good foundation but no exposure
            7-Good potential - Good foundation but limited exposure
            8- Good potential - Good foundation and experience
            9-Excellent potential - Exceed job Expectations
            10- Absolute Guru"""
}
response_llama_review = requests.post(url_llama_review, json=data_llama_review)


job_review = response_llama_review.json().get("response", "")        
print(job_review)