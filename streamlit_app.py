import streamlit as st

st.set_page_config(
    page_title="ILMORA",
    page_icon="📚",
    layout="wide"
)

st.markdown(
    """
    <div style="text-align:center; padding:40px 0;">
        <h1 style="font-size:52px; letter-spacing:3px;">
            ILMORA
        </h1>
        <p>RESEARCH. DISCOVER. VERIFY.</p>
        <p>AI-Assisted Islamic Research</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.subheader("What would you like to research?")

query = st.text_area(
    "Research question",
    placeholder="e.g. What do classical scholars say about patience?"
)

if st.button("Research"):
    if query.strip():
        st.write("Research interface is working.")
        st.write(f"Question: {query}")
    else:
        st.warning("Please enter a research question.")
