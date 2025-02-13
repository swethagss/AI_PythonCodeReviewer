
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key = api_key)

sys_prompt = """
You are a Python code reviewer. You can ONLY review Python code.
If someone asks non-Python questions reply:
'Sorry, I can only assist with Python code-related queries.' 
Do NOT attempt to answer unrelated questions
"""

model = genai.GenerativeModel(
    model_name= 'models/gemini-2.0-flash-exp',
    system_instruction = sys_prompt
)

st.set_page_config(page_title="AI Python Code Reviewer", layout="wide")

#Side Bar
st.sidebar.title("Welcome 👋")
st.sidebar.write("""
🔹 **About this App:**  
- 🔍 Review Python code for bugs and inefficiencies.
- 🛠 Get improved code snippets with explanations.
- 💬 Ask any Python related coding questions.              

🔹 **How to Use:**
1. Enter Python code in the text box.
2. Click '**Review Code**' button.
3. View the response below.
""")

# Main title
st.title("🤖 AI Python Code Reviewer")
st.subheader("Paste your Python code below 👇")

user_code = st.text_area("Enter Python Code:", height = 250)

if st.button("Review Code"):
    if user_code.strip():  # If input is not empty
        with st.spinner("Reviewing your code..."):
            response = model.generate_content(f"Review this Python code and provide a corrected version:\n{user_code}")

            # Splitting explanation and code fix
            response_text = response.text  # Full response from AI
            if "```python" in response_text:
                explanation, corrected_code = response_text.split("```python", 1)
                corrected_code = "```python" + corrected_code  # Re-add the code block syntax
            else:
                explanation = response_text
                corrected_code = "```python\n# No corrections needed or AI couldn't find errors.\n```"

            # Display explanation first
            st.markdown(f"**🔍 Issue in Your Code:**\n\n{explanation.strip()}")

            # Display corrected code in a separate box
            st.markdown(corrected_code)

    else:
        st.warning("⚠️ Please enter some Python code to review!")




    

