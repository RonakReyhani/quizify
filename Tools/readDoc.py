from transformers import Tool


def readDoc(file_name):
    with open(file_name) as f:
        return f.read()


class file_reader(Tool):
    name = "file_reader_tool"
    description = "This is a tool for reading a text file content. It takes an input named `file_name` and returns the text content of the file."
    input = ["text"]
    output = ["text"]

    def __call__(self, file_name: str):
        return readDoc(file_name)


file_reader_tool = file_reader()
