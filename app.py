import streamlit as st
from graph import app

st.title("Cortex AI")
st.subheader("Multi-Agent Research Assistant")

question = st.text_input("Enter your research question:")

if st.button("Research"):
    if question:
        with st.spinner("Researching..."):
            result = app.invoke({"question": question})
        st.markdown(result["answer"])
    else:
        st.warning("Please enter a question.")