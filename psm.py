import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="Password Strength Checker 🚀",
    page_icon="🔒",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {
        width: 50%; 
        background-color: orange; 
        color: white; 
        font-size: 18px; 
        border-radius: 8px; 
        padding: 10px;
    }
    .stButton button:hover {
        background-color: blue; 
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔑 Password Strength Checker")
st.write("🔍 Enter your password below to evaluate its security level.")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🚫 Password must be at least **8 characters long**.")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔤 Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Password should include **at least one number (0-9)**.")

    # Special character check
    if re.search(r"[!@#$%^&*?]", password):
        score += 1
    else:
        feedback.append("❗ Include **at least one special character (!@#$%^&*?)**.")

    # Display password strength results
    if score == 4:
        st.success("🌟 **Strong Password** - Your password is highly secure!")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving it for better security.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to make it stronger.")

    # Feedback
    if feedback:
        with st.expander("💡 **Password Suggestions**:"):
            for item in feedback:
                st.write(item)

# User input for password
password = st.text_input(
    "🔐 Enter your password:",
    type="password",
    help="Ensure your password is strong and secure!"
)

# Button functionality
if st.button("✅ Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
