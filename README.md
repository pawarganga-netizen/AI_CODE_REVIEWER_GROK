# AI_CODE_REVIEWER_GROK
AI Code Reviewer built with Streamlit and the Grok API. Reviews Python code, detects bugs, suggests improvements, and provides optimization recommendations through an interactive web interface with a clean and user-friendly design.

# 💻 AI Code Reviewer using Grok API

An AI-powered Code Reviewer built with **Streamlit** and the **Grok API**. This application analyzes Python code, identifies potential bugs, suggests improvements, and recommends best coding practices to help developers write cleaner and more efficient code.


## 🚀 Features

- 🔍 AI-powered code review
- 🐞 Detects potential bugs and issues
- ✨ Suggests code improvements
- 📖 Recommends best coding practices
- ⚡ Simple and interactive Streamlit interface
- 🤖 Powered by the Grok API


## 🛠️ Tech Stack

- Python
- Streamlit
- Grok API
- OpenAI Python SDK
- Python-dotenv


## 📂 Project Structure

```
AI_CODE_REVIEWER_GROK/
│── app.py
│── code_reviewer.py
│── prompt.py
│── requirements.txt
│── .env.example
│── README.md


## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI_CODE_REVIEWER_GROK.git

### 2. Navigate to the project

```bash
cd AI_CODE_REVIEWER_GROK

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate

### 4. Install dependencies

```bash
pip install -r requirements.txt

### 5. Configure API Key

Create a `.env` file in the project directory.

```env
GROK_API_KEY=your_api_key_here

## ▶️ Run the Application

```bash
streamlit run app.py

The application will open automatically in your browser.


## 📸 Demo

Paste your Python code into the text area and click **Review Code** to receive AI-generated feedback.


## 📌 Future Improvements

- Support multiple programming languages
- Code complexity analysis
- Security vulnerability detection
- Downloadable review reports
- Syntax highlighting
- Code quality score


## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.


## 📄 License

This project is licensed under the MIT License.
