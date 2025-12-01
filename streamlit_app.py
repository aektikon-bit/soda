
import streamlit as st

# ฟังก์ชั่นสำหรับคำนวณเกรด
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# ตั้งชื่อแอป
st.title("Grade Calculator")

# ข้อมูลจากผู้ใช้
score = st.number_input("กรุณากรอกคะแนนของคุณ (0-100):", min_value=0, max_value=100)

# คำนวณเกรด
if score >= 0:
    grade = calculate_grade(score)
    st.write(f"เกรดของคุณคือ: {grade}").
