import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="SmartFit-Student AI", layout="centered")

st.title("🎓 SmartFit-Student")
st.caption("Constraint-Aware Explainable AI Fitness Planner for Students")

api_key = st.sidebar.text_input("Gemini API Key", type="password")

model = None

if api_key:
    genai.configure(api_key=api_key)

    models = [
        m.name for m in genai.list_models()
        if "generateContent" in m.supported_generation_methods
    ]

    if models:
        model = genai.GenerativeModel(models[0])
    else:
        st.error("No compatible Gemini models available for this API key.")

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
    if not api_key:
        st.error("Please enter your Gemini API key.")
    elif not model:
        st.error("No usable Gemini model found for your API key.")
    else:
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

Generate:
1. Personalized Workout Plan
2. Practical Meal Strategy
3. Explanation
4. Fallback Plan
5. 3 Micro-Habits

Rules:
- No supplements
- Student-friendly
- Realistic
- No gym jargon
"""

        with st.spinner("Thinking like a student-friendly AI..."):
            response = model.generate_content(prompt)

        st.subheader("📘 Your SmartFit Plan")
        st.write(response.text)
