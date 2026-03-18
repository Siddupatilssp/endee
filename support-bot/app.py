import streamlit as st
from search_engine import search_answer

st.set_page_config(page_title="AI Support Chatbot", layout="wide")

st.title("🤖 AI Customer Support Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# User input
query = st.chat_input("Type your question...")

if query:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").write(query)

    # Get response
    answers = search_answer(query)
    response = " ".join(answers)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    "AI-powered customer support chatbot using semantic search concepts. "
    "Designed to automate and improve customer support experience."
)