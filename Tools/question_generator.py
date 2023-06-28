import random
from transformers import pipeline, Tool


def generate_questions_with_answers(document, num_questions=10):
    # Load the text2text-generation pipeline
    qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-base-qa-qg-hl")

    # Generate questions and answers from the document
    generated_pairs = []
    chunk_size = 512  # Adjust this value based on your specific requirements

    # Split the document into chunks of the desired size
    chunks = [document[i : i + chunk_size] for i in range(0, len(document), chunk_size)]

    # Generate questions and answers until reaching the desired number
    while len(generated_pairs) < num_questions:
        # Select a random chunk from the document
        chunk = random.choice(chunks)

        # Generate question and answer using the text2text-generation pipeline
        qg_input = "generate question: " + chunk
        generated_text = qg_pipeline(qg_input, max_length=64, num_return_sequences=1)

        # Extract the generated question from the pipeline response
        question = generated_text[0]["generated_text"].strip()

        # Generate answer using the text2text-generation pipeline
        qa_input = "answer: " + question + " context: " + chunk
        generated_text = qg_pipeline(qa_input, max_length=64, num_return_sequences=1)

        # Extract the generated answer from the pipeline response
        answer = generated_text[0]["generated_text"].strip()

        # Ensure the generated question-answer pair is unique
        if (question, answer) not in generated_pairs:
            generated_pairs.append((question, answer))

    return generated_pairs


# for question, answer in generated_pairs:
#     print("Question:", question)
#     print("Answer:", answer)
#     print()


class question_generator(Tool):
    name = "questtion_generator_tool"
    description = "This is a tool for generating question and answers from a long document. It takes an input named `document` and an input named `numb_questions`,and returns a list of question and answer pairs."
    input = ["text", "int"]
    output = ["text"]

    def __call__(self, document: str, num_questions):
        return generate_questions_with_answers(document, num_questions)


questtion_generator_tool = question_generator()
