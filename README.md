# Mistral Code Explainer

**Mistral Code Explainer** is a Generative AI-powered web application that explains code in simple, beginner-friendly English.  
Built using Python and Streamlit, it leverages the open-source Mistral 7B language model via [OpenRouter.ai](https://openrouter.ai) to turn code into natural language explanations.

Whether you're a student trying to learn programming, a junior developer understanding unfamiliar code, or an educator preparing annotated examples — this tool is designed to make code more understandable for everyone.

---

## 🔍 How It Works

1. The user pastes a Python or JavaScript code snippet into the app.
2. The app sends the code to the Mistral 7B model through the OpenRouter API.
3. The model returns an explanation in plain English.
4. The explanation is displayed in a readable format via Streamlit.

---

## ✅ Features

- Accepts any code snippet (Python, JavaScript, and others)
- Uses Mistral 7B Instruct (via OpenRouter) for explanation
- Explains logic, control flow, and function behavior in plain English
- Fast, lightweight, and completely free to use
- Built with a minimal, responsive UI using Streamlit

---

## 🛠 Technologies Used

| Layer       | Technology / Tool               |
|-------------|----------------------------------|
| Frontend    | Streamlit (Python web framework) |
| Backend     | OpenRouter API (Mistral 7B)      |
| Language    | Python                           |
| API Client  | `requests` library               |

---
