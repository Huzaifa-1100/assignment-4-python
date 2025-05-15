import streamlit as st

# BMI Calculator Page
st.title("📊 BMI Calculator")

st.write("""
Use this tool to calculate your Body Mass Index (BMI) based on your weight and height.
""")

# User Input: Weight (kg)
weight = st.slider("Enter your weight (in kg):", min_value=30.0, max_value=200.0, value=70.0, step=0.1)

# User Input: Height (cm)
height_cm = st.slider("Enter your height (in cm):", min_value=100.0, max_value=250.0, value=170.0, step=0.1)

# Convert height from cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

# Display BMI Result
st.subheader(f"Your BMI is: {bmi:.2f}")

# Interpretation of BMI
if bmi < 18.5:
    st.error("Underweight: You may need to gain some weight.")
elif 18.5 <= bmi < 24.9:
    st.success("Normal weight: Great job! Keep maintaining a healthy lifestyle.")
elif 25 <= bmi < 29.9:
    st.warning("Overweight: Consider adopting healthier habits.")
else:
    st.error("Obesity: It's important to consult a healthcare professional.")

st.write("""
---
Made with ❤️ by [Your Name]
""")