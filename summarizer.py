from transformers import pipeline

# Load T5 summarizer model (run once)
summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text, max_chunk=500):
    # Split large text into chunks
    paragraphs = text.split("\n")
    summaries = []

    current_chunk = ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_chunk:
            current_chunk += " " + para
        else:
            summaries.append(summarizer(current_chunk.strip())[0]['summary_text'])
            current_chunk = para
    if current_chunk:
        summaries.append(summarizer(current_chunk.strip())[0]['summary_text'])

    return summaries
