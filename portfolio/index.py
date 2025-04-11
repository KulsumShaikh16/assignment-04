import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Kulsum's Portfolio", page_icon=":sparkles:", layout="centered")

    # --- Header ---
    st.title("Hey, I'm Kulsum 👋")
    st.subheader("Beginner Python & Web Developer")
    st.write("Welcome to my Python-powered portfolio! Made with Streamlit 💻")

    # --- Profile Photo ---
    image = Image.open("profile.jpg")  # Make sure you have a profile.jpg file
    st.image(image, width=200)

    # --- About Me ---
    st.header("About Me")
    st.write("""
    I'm learning Python, Streamlit, and building cool beginner projects like:
    - BMI Calculator 🧮
    - Rock, Paper, Scissors 🎮
    - Guess the Number 🎯
    - Password Generator  🔑
    - Hangman Python 🎤
    - Growth Mindset Challenge App 🚀
    - Countdown Timer ⏳
    - To-Do List App 📋
    - Unit Converter App 🔄
    - Student Results Generator 📊

    
    I'm passionate about personal development and building fun tools with code!
    """)

    # --- Skills ---
    st.header("Skills")
    st.write("- Python 🐍")
    st.write("- Streamlit 🌐")
    st.write("- HTML, CSS  🖌️")
    st.write("- JavaScript 🎮")
    st.write("- Typescript  📜")
    st.write("- WordPress 🧩")

    # --- Projects ---
    st.header("Projects")
    st.write("👉 [BMI Calculator Web App](https://body-mass-index-calculator.streamlit.app/)")
    st.write("👉 [Rock, Paper, Scissors Game](https://rock-paper-sci.streamlit.app/)")
    st.write("👉 [Growth Mindset Challenge App](https://growth-mindset-app-2.streamlit.app/)")
    st.write("👉 [Password Generator](https://password-generator-16.streamlit.app/)")
    st.write("👉 [Password Strength Meter](https://password-strength-meter-16.streamlit.app/))")
    st.write("👉 [Unit Converter](https://unit-converter-16.streamlit.app/)")

    # --- Contact ---
    st.header("Get in Touch")
    st.write("📧 kulsumshaikh1605@gmail.com")
    st.write("[GitHub](https://github.com/KulsumShaikh16) | [LinkedIn](https://linkedin.com/in/https://www.linkedin.com/in/kulsum-shaikh-725ab22a9/)")

if __name__ == "__main__":
    main()
