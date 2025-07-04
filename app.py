import streamlit as st
import requests

API_KEY = "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"
MODEL = "mistralai/mistral-7b-instruct"

st.set_page_config(page_title="Free AI Code Explainer", layout="centered")
st.title("🤖 Free AI Code Explainer (OpenRouter)")
st.markdown("Paste your Python or JavaScript code below to get a free GPT-3.5 explanation.")

code_input = st.text_area("📝 Enter your code here", height=300)

if st.button("🔍 Explain Code"):
    if not code_input.strip():
        st.warning("Please enter some code.")
    else:
        with st.spinner("Generating explanation..."):
            try:
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": MODEL,
                        "messages": [
                            {"role": "system", "content": "You are an assistant that explains code in simple language for beginners."},
                            {"role": "user", "content": f"Explain this code:\n\n{code_input}"}
                        ],
                        "temperature": 0.5
                    }
                )

                # ✅ Properly indented debug output
                st.write("Status Code:", response.status_code)
                st.write("Response:", response.text)

                data = response.json()
                explanation = data["choices"][0]["message"]["content"]
                st.success("✅ Explanation:")
                st.markdown(explanation)

            except Exception as e:
                st.error(f"❌ Error: {e}")
