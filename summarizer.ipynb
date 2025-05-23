{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "991dba29",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "# Load T5 summarizer model (run once)\n",
    "summarizer = pipeline(\"summarization\", model=\"t5-small\")\n",
    "\n",
    "def summarize_text(text, max_chunk=500):\n",
    "    # Split large text into chunks\n",
    "    paragraphs = text.split(\"\\n\")\n",
    "    summaries = []\n",
    "\n",
    "    current_chunk = \"\"\n",
    "    for para in paragraphs:\n",
    "        if len(current_chunk) + len(para) < max_chunk:\n",
    "            current_chunk += \" \" + para\n",
    "        else:\n",
    "            summaries.append(summarizer(current_chunk.strip())[0]['summary_text'])\n",
    "            current_chunk = para\n",
    "    if current_chunk:\n",
    "        summaries.append(summarizer(current_chunk.strip())[0]['summary_text'])\n",
    "\n",
    "    return summaries\n"
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
