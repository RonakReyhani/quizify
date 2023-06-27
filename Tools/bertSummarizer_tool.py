from transformers import BartTokenizer, BartForConditionalGeneration
from readPDF import read_pdf
from transformers import pipeline
import re
from transformers import Tool

# Function to remove noise from the summary
def remove_noise(summary):
    # Define patterns for noise removal
    patterns = [
        r"\bPage \d+\b",  # Remove page numbers
        r"\bReferences:\b",  # Remove references section
        # Add more patterns as per your specific requirements
    ]

    # Apply pattern matching to remove noise
    for pattern in patterns:
        summary = re.sub(pattern, "", summary)

    return summary.strip()
# Step 1: Summarize the document
def summarize_document(document):
    tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# Split the document into sentences
    sentences = document.split(".")
    chunk_size = 512  # Adjust the chunk size as needed
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += sentence + "."
        else:
            chunks.append(chunk.strip())
            chunk = sentence + "."
    if chunk:
        chunks.append(chunk.strip())

    # Generate summaries for each chunk
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=300, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)

    # Concatenate the summaries into a single summary
    final_summary = ' '.join(summaries)
    final_summary = remove_noise(final_summary)
    return final_summary


class summarize_service (Tool):
  name="summarizer_tool"
  description="This is a tool for summarizing text documents. It takes an input named `file_name`. It reads the document and returns the summarization of the document content as text."
  input=['text']
  output=['text']
  def __call__(self, file_name: str):
    return summarize_document(file_name)

summarizer_tool =  summarize_service()


# # Example usage
# DOCUMENT = read_pdf("../documents/summarize.pdf")

# # Step 1: Summarize the document without truncating sentences
# summary = summarize_document(DOCUMENT)

# # Print the result
# print("Summary:", summary)
