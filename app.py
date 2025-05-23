import streamlit as st
from pdf_parser import extract_text_from_pdf
from summarizer import summarize_text
from flashcard_gen import generate_flashcards

st.set_page_config(page_title="FlashForge", layout="wide")
st.title("📚 FlashForge - Turn PDFs into Flashcards with AI")

uploaded_file = st.file_uploader("Upload your textbook or slides (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        raw_text = extract_text_from_pdf(uploaded_file)

    st.success("Text extracted. Summarizing...")
    with st.spinner("Summarizing content..."):
        summaries = summarize_text(raw_text)

    st.success("Generating flashcards...")
    with st.spinner("Generating questions..."):
        flashcards = generate_flashcards(summaries)

    st.subheader("🧠 Generated Flashcards")
    for i, (q, a) in enumerate(flashcards):
        with st.expander(f"Q{i+1}: {q}"):
            st.markdown(f"**A:** {a}")

    if st.button("Download Flashcards"):
        content = "\n\n".join([f"Q: {q}\nA: {a}" for q, a in flashcards])
        st.download_button("📥 Download .txt", content, file_name="flashcards.txt")
