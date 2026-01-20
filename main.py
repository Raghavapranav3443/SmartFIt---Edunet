import streamlit as st
import google.generativeai as genai
import os

# Gemini configuration
genai.configure(api_key="AIzaSyBCIymWozMHX-IwT4ulitEkYerDQ2YI6Mk")
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.set_page_config(page_title="SmartFit-Student AI", layout="centered")

st.title("🎓 SmartFit-Student")
st.caption("Constraint-Aware Explainable AI Fitness Planner for Students")

st.markdown("### 👤 Student Profile")
age = st.number_input("Age", 16, 40)
weight = st.number_input("Weight (kg)", 30, 150)

st.markdown("### 🎯 Goals & Constraints")
goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "General Fitness"])
academic_load = st.selectbox("Current Academic Phase", ["Normal Classes", "Exam Period"])
time_available = st.selectbox("Daily Time Available", ["15–20 minutes", "20–30 minutes", "30–45 minutes"])
equipment = st.selectbox("Workout Equipment", ["No Equipment", "Gym Access"])

st.markdown("### 🍽️ Food Reality")
diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian"])
food_source = st.selectbox("Primary Food Source", ["Hostel Mess", "Home Food", "Outside Food"])
budget = st.selectbox("Food Budget", ["Low", "Medium"])

if st.button("Generate Smart Plan"):
    prompt = f"""
    You are an AI fitness system designed specifically for Indian college students.

    Student Profile:
    Age: {age}
    Weight: {weight} kg

    Constraints:
    - Fitness Goal: {goal}
    - Academic Phase: {academic_load}
    - Available Time: {time_available}
    - Equipment: {equipment}
    - Diet: {diet}
    - Food Source: {food_source}
    - Budget: {budget}

    Generate a plan with the following structure:

    1. Personalized Workout Plan (respecting time & academic load)
    2. Practical Meal Strategy (based on food source)
    3. Explanation Section:
       - Why this workout intensity was chosen
       - Why these food choices make sense
    4. Fallback Plan:
       - If workout is skipped
       - If meals go off-plan
    5. 3 Micro-Habits for consistency

    Rules:
    - No supplements
    - Student-friendly language
    - Realistic, not idealistic
    - Avoid gym jargon
    """

    with st.spinner("Thinking like a student-friendly AI..."):
        response = model.generate_content(prompt)

    st.subheader("📘 Your SmartFit Plan")
    st.write(response.text)
