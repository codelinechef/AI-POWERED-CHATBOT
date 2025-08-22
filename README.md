<h1 align="center">
  🤖 AI-Powered Command Line Assistant
</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/b1fd766e-1009-4abf-8a71-bb8178c6438b" alt="Google AI" width="220"/>
</p>


<p align="center">
  <b>Natural Language → System Command → Controlled Execution</b><br>
  Built with <strong>Google Gemini</strong>, <strong>Python</strong>, and <strong>Gradio</strong>
</p>

---

## 💡 Project Description

This project is a **smart, safe, AI-powered assistant** that turns your plain-English commands into actual shell commands and optionally executes them — with full safety controls.

### 🧠 Key Capabilities
- 🔍 Understands natural language tasks like "open YouTube" or "list files"
- 💡 Uses **Google Gemini 1.5 Flash** to suggest OS-specific commands
- 🛡️ Classifies commands as SAFE, DANGEROUS, or UNKNOWN
- ✅ Automatically runs safe commands; prompts for dangerous ones
- 🌐 Web-based GUI built using **Gradio**
- 🔌 Easily extensible via modular architecture

---

## 🧠 Tech Stack

| Tool | Role |
|------|------|
| ![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) | Core programming language |
| ![Google AI](https://img.shields.io/badge/Google-Gemini-red?logo=google) | LLM for prompt-to-command |
| ![Gradio](https://img.shields.io/badge/Gradio-UI-green?logo=gradio) | Web-based interface |
| ![dotenv](https://img.shields.io/badge/dotenv-SecureKeys-lightgrey?logo=dotenv) | Secret key management |

---

## ⚙️ Architecture

```plaintext
User Prompt
   ↓
Gemini Model ("gemini-1.5-flash")
   ↓
Command Suggestion (OS-aware)
   ↓
Safety Validator (safe/dangerous/unknown)
   ↓
Executor (shell or blocked)
```

## 🧑‍💻 Author

Anant Sharma
🔗 GitHub: https://github.com/codelinechef
