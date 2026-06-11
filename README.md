# EduTutor AI

EduTutor AI is a personalized learning assistant designed to support both students and teachers. It features two different modules: one utilizing the Gemini API (`Kaboom`) and another utilizing the IBM Granite NLP models (`edututor_ai`).

Both modules provide interactive Streamlit interfaces with specific functionalities tailored for students and teachers.

---

## 🚀 Features

### 🧑‍🎓 Student Interface
- **Personalized Learning**: Students can ask educational questions or request targeted learning content.
- **AI-Powered Explanations**: Uses state-of-the-art LLMs (Gemini / IBM Granite) to explain concepts clearly.

### 🧑‍🏫 Teacher Interface
- **Automated Grading**: Teachers can upload student assignments (text format) for grading.
- **Detailed Feedback**: Provides automated AI-driven grading and feedback report.

---

## 🛠️ Project Structure

- `Kaboom/` — Gemini API powered module.
  - `app.py`: Streamlit frontend application.
  - `ai_module_gemini.py`: Logic interfacing with the Gemini API.
  - `requirements.txt`: Python dependencies for this module.
- `edututor_ai/` — IBM Granite powered module.
  - `app.py`: Streamlit frontend application.
  - `ai_module_ibm.py`: Logic interfacing with IBM Granite models.
  - `edututor_ai_dev.ipynb`: Development notebook.
  - `requirements.txt`: Python dependencies for this module.

---

## ⚙️ Installation & Usage

### 1. Gemini Module (`Kaboom/`)
To run the Gemini-powered version:
```bash
cd Kaboom
pip install -r requirements.txt
streamlit run app.py
```

### 2. IBM Granite Module (`edututor_ai/`)
To run the IBM-powered version:
```bash
cd edututor_ai
pip install -r requirements.txt
streamlit run app.py
```
