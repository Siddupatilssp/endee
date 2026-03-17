import streamlit as st
from search_engine import search_answer

st.title("🤖 AI Customer Support Assistant")

query = st.text_input("Ask your question")

if query:
    answers = search_answer(query)
    
    st.subheader("💡 AI Response")
    
    for ans in answers:
        st.write("👉", ans)

    st.success("Answer generated using semantic search (Endee-based concept)")
    st.sidebar.title("About")
    
    st.sidebar.info(
    "This is an AI-powered customer support assistant using semantic search concepts. "
    "Designed to reduce manual support workload."
)