{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1451b8b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from pdf_parser import extract_text_from_pdf\n",
    "from summarizer import summarize_text\n",
    "from flashcard_gen import generate_flashcards\n",
    "\n",
    "st.set_page_config(page_title=\"FlashForge\", layout=\"wide\")\n",
    "st.title(\"📚 FlashForge - Turn PDFs into Flashcards with AI\")\n",
    "\n",
    "uploaded_file = st.file_uploader(\"Upload your textbook or slides (PDF)\", type=\"pdf\")\n",
    "\n",
    "if uploaded_file:\n",
    "    with st.spinner(\"Extracting text...\"):\n",
    "        raw_text = extract_text_from_pdf(uploaded_file)\n",
    "\n",
    "    st.success(\"Text extracted. Summarizing...\")\n",
    "    with st.spinner(\"Summarizing content...\"):\n",
    "        summaries = summarize_text(raw_text)\n",
    "\n",
    "    st.success(\"Generating flashcards...\")\n",
    "    with st.spinner(\"Generating questions...\"):\n",
    "        flashcards = generate_flashcards(summaries)\n",
    "\n",
    "    st.subheader(\"🧠 Generated Flashcards\")\n",
    "    for i, (q, a) in enumerate(flashcards):\n",
    "        with st.expander(f\"Q{i+1}: {q}\"):\n",
    "            st.markdown(f\"**A:** {a}\")\n",
    "\n",
    "    if st.button(\"Download Flashcards\"):\n",
    "        content = \"\\n\\n\".join([f\"Q: {q}\\nA: {a}\" for q, a in flashcards])\n",
    "        st.download_button(\"📥 Download .txt\", content, file_name=\"flashcards.txt\")\n"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
