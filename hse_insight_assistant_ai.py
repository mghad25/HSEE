import streamlit as st
import openai

st.set_page_config(page_title="HSE Insight Assistant", layout="centered")

st.title("🧠 HSE Insight Assistant with GPT")
st.write("Paste an incident report below. The assistant will summarize the event, identify the root cause, suggest corrective actions, and rate the severity using AI.")

api_key = st.text_input("🔑 Enter your OpenAI API key", type="password")

report_text = st.text_area("📄 Incident Report", height=300, placeholder="Paste your incident report here...")

def ask_gpt(prompt, api_key):
    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a health and safety AI assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

if st.button("🧠 Analyze with AI"):
    if not report_text.strip():
        st.warning("Please paste an incident report first.")
    elif not api_key:
        st.warning("Please enter your OpenAI API key.")
    else:
        prompt = f"""Analyze this HSE incident report. Provide:
1. A 2-3 sentence summary
2. The root cause
3. Suggested corrective or preventive actions
4. Severity rating (Minor, Moderate, Severe)

Report:
{report_text}"""
        result = ask_gpt(prompt, api_key)
        st.subheader("🤖 AI Response")
        st.write(result)
