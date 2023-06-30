from transformers import MarianMTModel, MarianTokenizer
from transformers import Tool

# Step 2: Translate the summary
def translate_text(text, target_lang, source_lang="en", max_chunk_length=512):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Split the text into smaller chunks
    chunks = [
        text[i : i + max_chunk_length] for i in range(0, len(text), max_chunk_length)
    ]

    translated_text = []

    # Translate each chunk individually
    for chunk in chunks:
        inputs = tokenizer(
            chunk, truncation=True, padding="longest", return_tensors="pt"
        )
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask

        translated = model.generate(input_ids=input_ids, attention_mask=attention_mask)

        translated_chunk = tokenizer.batch_decode(translated, skip_special_tokens=True)
        translated_text.extend(translated_chunk)

    return " ".join(translated_text)




# # Step 1: Translate the text
# translated_text = translate_text(text, source_lang, target_lang)
# print(translated_text)


class translate_my_text(Tool):
    name = "translate_text_tool"
    description = "This is a tool for translating a text file content. It takes two inputs, first the file content as text, then the target language. It translates the content and returns the result as text"
    input = ["text", "text"]
    output = ["text"]

    def __call__(self, txt: str, target_lang: str):
        return translate_text(txt, target_lang)


translate_text_tool = translate_my_text()
