import streamlit as st

# Contact Form Page
st.title("📧 Contact Us")

st.write("""
Feel free to reach out to us with any questions or feedback. Fill out the form below, and we'll get back to you soon!
""")

# Form Inputs
name = st.text_input("Your Name:")
email = st.text_input("Your Email:")
message = st.text_area("Your Message:")

# Submit Button
if st.button("Submit"):
    if name and email and message:
        st.success("Thank you for your message! We'll get back to you soon.")
    else:
        st.error("Please fill out all fields before submitting.")