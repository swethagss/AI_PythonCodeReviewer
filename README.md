# **🤖 AI Python Code Reviewer**

A **Streamlit-powered app** that reviews Python code for bugs and inefficiencies using **Google Gemini AI**. It provides bug reports, improved code snippets, and explanations to help developers write better code.

## **🔹Features**
- ✅ **Detect Bugs & Errors** – AI identifies potential issues in Python code.
- ✅ **Suggest Fixes** – Provides corrected code snippets with explanations.
- ✅ **User-Friendly UI** – Simple interface built with Streamlit.
- ✅ **Instant Feedback** – Get AI-powered insights in real-time.
- ✅ **Handles Only Python Queries** – Strictly focused on Python-related questions.

## **🖥️ Tech Stack**
- Python
- Streamlit
- Google Gemini AI
- Dotenv

## **Setup Instructions**
**1. Clone the Repository**
```
git clone <repository-url>
cd <repository-folder>
```

**2. Install Dependencies**
```
pip install -r requirements txt
```

**3. Create a ```.env``` file:** 
Add your Google API key to the ```.env``` file.
```
GOOGLE_API_KEY=your_google_api_key_here
```
**4. Run the Streamlit app:** 
After installing the required libraries and setting up the .env file, run the app using:
```
streamlit run app.py
```

[https://github.com/user-attachments/assets/e853eb77-0839-4905-8a77-f9169af2a7c1](https://github.com/user-attachments/assets/9ae4d909-e2f8-438d-882a-75089ab0e630)

## **How It Works**
1. Paste your Python Code - Enter your python code in the text box
2. Click 'Review Code' - AI will analyze the code and detects errors
3. Get the feedback - See for issues, explanations and corrected code

## **Example**
**🔻 Input Code with Error:**
```
def add(a,b):
  return a+b
result = add(5)
print("Sum:", result)
```
**✅ AI Suggested fix:**
```
def add(a,b):
  return a+b
result = add(5,3)
print("Sum:", result)
```


