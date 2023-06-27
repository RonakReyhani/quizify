import fitz
from transformers import Tool


def read_pdf(filename):
    context = ""
    # Open the PDF file
    with fitz.open(f"{filename}") as pdf_file:
        # Get the number of pages in the PDF file
        num_pages = pdf_file.page_count

        # Loop through each page in the PDF file
        for page_num in range(num_pages):
            # Get the current page
            page = pdf_file[page_num]

            # Get the text from the current page
            page_text = page.get_text()

            # Append the text to context
            context += page_text
    return context


class read_file(Tool):
    name = "read_file_tool"
    description = "This is a tool for reading documents (pdf) from the disk. It takes an input named `file_name` which should be the name of the file containing the document (pdf). It reads the document and returns the content of the document as text."
    input = ["text"]
    output = ["text"]

    def __call__(self, file_name: str):
        return read_pdf(file_name)


read_file_tool = read_file()
