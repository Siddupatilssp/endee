import streamlit as st
from search_engine import search_answer

st.title("AI Customer Support Bot")

query = st.text_input("Ask your question")

if query:
    answers = search_answer(query)
    for ans in answers:
        st.write("👉", ans)