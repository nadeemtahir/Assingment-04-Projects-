import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️‍♂️", layout="centered")

# --- BMI Calculation ---
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)

def show_bmi_result(bmi):
    st.subheader(f"🎯 Your BMI is: `{bmi}`")

    if bmi < 16:
        st.error("🚨 **Severely Underweight** – Please consult a healthcare provider.")
    elif bmi < 18.5:
        st.warning("⚠️ **Underweight** – Consider improving nutrition.")
    elif bmi < 25:
        st.success("✅ **Healthy Weight** – Great job! Maintain your lifestyle. 🏆")
    elif bmi < 30:
        st.warning("⚠️ **Overweight** – Focus on regular exercise and a balanced diet.")
    else:
        st.error("🚨 **Obese** – It's important to seek medical advice and plan weight management.")

# --- BMI Category Table ---
def show_bmi_categories():
    st.markdown("### 📊 BMI Categories & Health Tips")
    bmi_data = {
        "Category": [
            "Severely Underweight",
            "Underweight",
            "Healthy Weight",
            "Overweight",
            "Obese"
        ],
        "BMI Range": [
            "< 16",
            "16 - 18.4",
            "18.5 - 24.9",
            "25 - 29.9",
            "30+"
        ],
        "Health Tips": [
            "Increase calorie intake & seek medical advice.",
            "Eat nutritious food and gain weight gradually.",
            "Maintain your current routine! 👍",
            "Add regular workouts & track diet.",
            "Consult a healthcare professional."
        ]
    }

    df = pd.DataFrame(bmi_data)
    st.dataframe(df, use_container_width=True)

# --- App UI ---
def main():
    st.title("🏋️‍♂️ BMI Calculator")
    st.caption("Track your **Body Mass Index** and gain insights about your health.")

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            weight = st.slider("⚖️ Your Weight (kg)", 30, 150, step=1)
        with col2:
            height = st.slider("📏 Your Height (cm)", 100, 200, step=1)

    if st.button("🔍 Calculate My BMI"):
        bmi = calculate_bmi(weight, height)
        st.divider()
        show_bmi_result(bmi)

    st.divider()
    show_bmi_categories()

# --- Run App ---
if __name__ == '__main__':
    main()
