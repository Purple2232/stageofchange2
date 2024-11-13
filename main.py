import streamlit as st

# App title and introduction
st.title("Supporting Your Health with Screen and Light Use")
st.write("""
This tool helps you understand your daily screen use habits, assesses your readiness to manage potential health impacts, and provides tailored resources and strategies to support you in a positive, non-judgmental way.
""")

# Section 1: Screen Use Habits Assessment
st.header("Step 1: Understand Your Screen Use Habits")

# Question 1: Estimated hours of daily screen time
screen_time = st.selectbox("How many hours a day do you estimate you spend with screens?", 
                           options=["Less than 2 hours", "2-4 hours", "4-6 hours", "6-8 hours", "More than 8 hours"])

# Question 2: Devices frequently used
devices = st.multiselect("Which of these devices do you interact with daily? Select all that apply.",
                         options=["Smartphone", "Tablet", "Laptop", "Desktop Computer", "Television", "Other"])

# Question 3: Awareness of potential health effects
awareness = st.radio("Are you aware of any potential health impacts from frequent screen use?",
                     options=["Yes, I am aware", "No, I am not aware", "I've heard some information"])

# Question 4: Experiencing any health effects
health_effects = st.multiselect("Do you experience any of these related health effects? Select all that apply.",
                                options=["Difficulty sleeping", "Headaches", "Eye strain", "Neck or shoulder pain", "None of these"])

# Question 5: Have you tried any methods to manage screen use?
manage_screen_time = st.radio("Have you tried anything to manage your screen time or reduce screen-related health impacts?",
                              options=["Yes", "No"])

# Calculate the initial Screen Use Score
score = 0
if screen_time == "Less than 2 hours":
    score += 10
elif screen_time == "2-4 hours":
    score += 25
elif screen_time == "4-6 hours":
    score += 50
elif screen_time == "6-8 hours":
    score += 75
else:
    score += 90
score += len(devices) * 5
if awareness != "No, I am not aware":
    score += 10
score += len(health_effects) * 5
if manage_screen_time == "Yes":
    score -= 10
score = min(score, 100)

# Display score and provide initial feedback
st.write("### Your Screen Use Score: ", score, "%")
if score > 50:
    st.write("Your screen use is above average. Below, we’ll provide personalized tips to help balance screen habits in a supportive way.")

# Section 2: Readiness Assessment
st.header("Step 2: Assess Your Readiness to Make Changes")

# Questions to determine stage of readiness
readiness_awareness = st.radio("How familiar are you with potential health impacts of prolonged screen and light use?",
                               options=["Not familiar", "Somewhat familiar", "Quite familiar"])

readiness_desire = st.radio("How interested are you in learning more or taking steps to mitigate any health impacts?",
                            options=["Not interested", "Considering it", "Would like to but unsure how", "Actively taking steps"])

readiness_actions_taken = st.radio("Have you already taken any steps to reduce potential health impacts of screen and light use?",
                                   options=["None", "Thinking about it", "Some steps", "Consistent changes"])

# Determine readiness stage based on responses
if readiness_awareness == "Not familiar" and readiness_desire == "Not interested":
    stage = "New to the Topic"
elif readiness_awareness == "Somewhat familiar" and readiness_desire in ["Considering it", "Would like to but unsure how"]:
    stage = "Curious but Unsure"
elif readiness_awareness == "Quite familiar" and readiness_desire == "Would like to but unsure how":
    stage = "Aware but Seeking Guidance"
elif readiness_awareness == "Quite familiar" and readiness_desire == "Actively taking steps" and readiness_actions_taken in ["Some steps", "Consistent changes"]:
    stage = "Taking Positive Steps"
else:
    stage = "Balanced and Knowledgeable"

# Section 3: Personalized Guidance Based on Readiness Stage
st.header("Step 3: Your Personalized Support and Recommendations")
st.write(f"Based on your responses, you are in the **{stage}** stage.")

# Provide resources and suggestions based on stage
if stage == "New to the Topic":
    st.write("""
    It seems you're new to the topic of managing health impacts from screen and light exposure. Here’s some initial information to get started:
    - **Health Effects**: Prolonged screen time can impact sleep, cause eye strain, and contribute to headaches.
    - **Simple Tips**: Try the 20-20-20 rule, move around every hour, and spend a few minutes outside each day.
    - **Resources**:
        - [National Sleep Foundation](https://www.sleepfoundation.org)
        - [American Optometric Association](https://www.aoa.org)
    """)

elif stage == "Curious but Unsure":
    st.write("""
    You’re interested in making changes but may not know where to start. Here are some easy adjustments:
    - **Night Mode or Blue Light Filters**: Use these on devices to reduce eye strain.
    - **Reduce Evening Screen Time**: Limiting screen use before bed can improve sleep.
    - **Resources**:
        - [Flux (Blue Light Filter)](https://justgetflux.com)
        - [Eye Exercises](https://www.allaboutvision.com/conditions/eye-exercises/)
    """)

elif stage == "Aware but Seeking Guidance":
    st.write("""
    You’re aware of the health impacts and want to make changes. Here are some strategies to get started:
    - **Blue Light Glasses**: Helpful if you often work or study at night.
    - **Lighting Adjustments**: Use softer lighting in the evening to minimize eye strain.
    - **Resources**:
        - [Zenni Blue Light Glasses](https://www.zennioptical.com/b/blue-light-glasses)
        - [Light Therapy Guide](https://www.sleepfoundation.org/circadian-rhythm/light-therapy)
    """)

elif stage == "Taking Positive Steps":
    st.write("""
    You’re already taking positive steps! Here’s guidance to support ongoing improvement:
    - **Movement and Eye Exercises**: Incorporate stretches or walks to reduce strain.
    - **Ambient Lighting**: Use warm lights in the evening and maximize daylight in the morning.
    - **Resources**:
        - [American Academy of Ophthalmology Exercises](https://www.aao.org/eye-health/tips-prevention/computer-usage)
        - [Philips Hue Adjustable Lighting](https://www.philips-hue.com)
    """)

elif stage == "Balanced and Knowledgeable":
    st.write("""
    You’re well-informed and have created a balanced routine. Here are a few advanced tips:
    - **Mindfulness Breaks**: Incorporate mindfulness during screen breaks.
    - **Advanced Lighting Control**: Try smart lighting systems that mimic natural daylight cycles.
    - **Resources**:
        - [Calm Meditation App](https://www.calm.com)
        - [Lightmeter App for Brightness Tracking](https://lightmeter.app)
    """)

# Closing message
st.write("""
Thank you for exploring ways to support your screen use health. We hope these insights and resources provide helpful guidance on your wellness journey.
""")
