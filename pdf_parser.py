{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "958acbdf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitz  # PyMuPDF\n",
    "\n",
    "def extract_text_from_pdf(file):\n",
    "    doc = fitz.open(stream=file.read(), filetype=\"pdf\")\n",
    "    text = \"\"\n",
    "    for page in doc:\n",
    "        text += page.get_text()\n",
    "    return text\n"
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
