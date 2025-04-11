import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def main():
    st.title("💪 BMI Calculator")
    st.write("Calculate your Body Mass Index easily!")

    # ✅ Add unique keys to avoid StreamlitDuplicateElementId
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, key="weight_input")
    height = st.number_input("Enter your height (m):", min_value=0.1, key="height_input")

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.success(f"Your BMI is: {bmi}")

        # Show category
        if bmi < 18.5:
            st.info("You are underweight.")
        elif 18.5 <= bmi < 25:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 30:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

if __name__ == "__main__":
    main()
