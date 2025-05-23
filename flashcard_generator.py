{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "036870ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "# Question generation pipeline\n",
    "qg_pipeline = pipeline(\"text2text-generation\", model=\"iarfmoose/t5-base-question-generator\")\n",
    "\n",
    "def generate_flashcards(summary_chunks):\n",
    "    flashcards = []\n",
    "    for chunk in summary_chunks:\n",
    "        question = qg_pipeline(\"generate question: \" + chunk)[0]['generated_text']\n",
    "        flashcards.append((question, chunk))\n",
    "    return flashcards\n"
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
