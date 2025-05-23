from transformers import pipeline

# Question generation pipeline
qg_pipeline = pipeline("text2text-generation", model="iarfmoose/t5-base-question-generator")

def generate_flashcards(summary_chunks):
    flashcards = []
    for chunk in summary_chunks:
        question = qg_pipeline("generate question: " + chunk)[0]['generated_text']
        flashcards.append((question, chunk))
    return flashcards
