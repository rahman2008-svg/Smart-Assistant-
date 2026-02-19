import streamlit as st
import os
from openai import OpenAI

# অ্যাপের টাইটেল
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖")
st.title("🤖 My Custom ChatGPT")

# Render থেকে API Key নেওয়া (নিরাপদ পদ্ধতি)
api_key = os.environ.get("GROK_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.x.ai/v1",
)

# চ্যাট হিস্ট্রি স্টোর করা
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ইউজার ইনপুট
if prompt := st.chat_input("আপনি কী জানতে চান?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI এর উত্তর জেনারেট করা
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="grok-2",
             # অথবা আপনার কেনা মডেলের নাম
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
  
