from transformers import pipeline, T5Tokenizer, AutoModelForSeq2SeqLM
# Question generation pipeline
model_name = "iarfmoose/t5-base-question-generator"
tokenizer = T5Tokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

qg_pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)


def generate_flashcards(summary_chunks):
    flashcards = []
    for chunk in summary_chunks:
        question = qg_pipeline("generate question: " + chunk)[0]['generated_text']
        flashcards.append((question, chunk))
    return flashcards
