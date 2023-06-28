from huggingface_hub import login
from transformers import HfAgent
import pandas as pd
import streamlit as st
import downloader as downloader
import readPDF as fileReader
import bertSummarizer_tool as summarizer
import question_generator as quizzer
import translator_tool as translator
import audio_generator as speaker


# ---------------------------- login to huggingface hub and set up---------------------#
token = st.secrets["hugging_face_token"]
login(token)

tools = [
    downloader.download_file_tool,
    fileReader.read_file_tool,
    summarizer.summarizer_tool,
    translator.translate_text_tool,
    speaker.text_to_speech_tool,
]
agent = HfAgent(
    "https://api-inference.huggingface.co/models/bigcode/starcoder",
    additional_tools=tools,
)


def get_session_state():
    return st.session_state


# Initialize session state
session_state = get_session_state()
if "download_file_ready" not in session_state:
    session_state.download_file_ready = False
if "summarised_clicked" not in session_state:
    session_state.summarised_clicked = False
if "file_name" not in session_state:
    session_state.file_name = None
if "file_content" not in session_state:
    session_state.file_content = None
if "file_translation" not in session_state:
    session_state.file_translation = None
if "file_summary" not in session_state:
    session_state.file_summary = None
if "file_voice" not in session_state:
    session_state.file_voice = None


# --------------------------------------------------Helper functions---------------------------------#
def set_clicked_upload_file():
    session_state.download_file_ready = True


def set_summarised_clicked():
    session_state.summarised_clicked = True


def download(url):
    return agent.run(f"Download file from the web {url}", url=url)


# ----------------------------------------------------- Page Components ------------------------------------#
st.title("Empowering Self-Service Learning with Hugging Face Transformers")
st.divider()
st.header("Introduction")
st.markdown(
    "The ` Self-Service Learning platform` is an innovative app designed to revolutionize your learning experience. With this powerful tool, users can effortlessly generate custom quizzes based on any PDF file they download from the web.\nGone are the days of tedious manual summarization and translation! Our app leverages the cutting-edge capabilities of Hugging Face transformers to simplify the entire process. Once you've obtained a PDF, simply import it into the app and watch as the magic unfolds."
)
st.markdown(
    "The  Self-Service Learning platform empowers you to summarize the document with ease, condensing its key points into a concise format. Not only that, but our app also offers built-in translation functionality, allowing you to understand the content in your preferred language.\n But the true power of our app lies in its ability to transform your summarized and translated document into an interactive multi-choice quiz."
)
st.markdown(
    "By analyzing the text and extracting relevant information, the app generates thought-provoking questions that test your understanding of the material.\n Whether you're a student striving for academic excellence or a professional looking to enhance your knowledge, the Self Service Quiz Generator platform is your go-to tool for efficient and engaging learning. Experience the convenience, accuracy, and effectiveness of our app today and take your learning journey to new heights."
)
st.divider()

# --------------------------------------- Enter URL -----------------------------------------#
st.header("Downloader, Uploader Service")
st.markdown(
    "To begin, you have two options: either upload the file directly or provide a valid URL for your PDF resource."
)
st.markdown(
    "If you choose to enter a URL, our advanced Hugging Face Agent will seamlessly download the file for you. This process utilizes a specialized tool known as the `download_file_tool` working silently behind the scenes to retrieve the document."
)
st.markdown("Currently, our platform exclusively supports PDF files at this stage.")
url = st.empty()
url = st.text_input("Enter a valid URL:")

col1, col2, col3, col4 = st.columns([0.4, 0.2, 0.3, 0.3])
with col1:
    pass
with col2:
    pass
with col3:
    upload_file_url = st.button("Upload From Web", on_click=set_clicked_upload_file)
with col4:
    # download_file = st.button(
    #     label="Download PDF",
    #     disabled=not session_state.download_file_ready,
    # )
    download_file = st.download_button(
        label="DOWNLOAD FILE", data="pdf", file_name=url, mime="text/pdf"
    )
    if url and download_file and session_state.download_file_ready:
        result = download(url)
        session_state.download_file_ready = False
        session_state.file_name = result
        st.write("Your file downloaded successfully")

# --------------------------------------- Upload File -----------------------------------------#
st.markdown(
    "As an alternative, you have the option to upload your PDF file. Our agent will utilize a specialized tool called `read_file_tool` to process and extract the content from the document. The extracted information will be saved for further use within the platform."
)
browse_upload_file = st.file_uploader("Choose a file", type=["pdf"])
if browse_upload_file is not None:
    # # To read file as bytes:
    bytes_data = browse_upload_file.read()
    file_name = browse_upload_file.name
    with open(file_name, "wb") as f:
        f.write(bytes_data)
st.divider()

# --------------------------------------- Summarize the content -----------------------------------------#
st.header("Summarization Service")
st.markdown(
    "And now, let the fun begin! Get ready to dive into the exciting features of our app. How about downloading a summarization of your uploaded document or web content? Let's embark on this thrilling journey together!"
)

st.markdown(
    "By clicking the `summarize` button below, the Hugging Face agent will generate a summary of your document. Please note that the summarization model used by the agent is the default tool, so the results may not be perfect. If your document is excessively large, there is a chance it may encounter difficulties or exhibit unexpected behavior while processing."
)
st.markdown(
    "And hey, I haven't forgotten about that! You might be eager to download the summary, so go ahead and click the button to access it."
)

col1, col2, col3, col4 = st.columns([0.4, 0.2, 0.3, 0.3])
with col1:
    pass
with col2:
    pass
with col3:
    summarise_button = st.button("Summarize", on_click=set_summarised_clicked)
with col4:
    btn = st.download_button(
        label="DOWNLOAD FILE", data="pdf", file_name=url, mime="text/pdf"
    )
    # download_summary_button = st.button(
    #     "Download Summary",
    #     disabled=not session_state.summarised_clicked,
    #     on_click=downloader(),
    # )
    if url and btn and session_state.summarised_clicked:
        session_state.file_name = result
st.divider()

# --------------------------------------- Translate the content -----------------------------------------#
st.markdown(
    "Hmmm, perhaps English is your second language, just like mine! But don't worry, I've got your back 😉. With this tool, you can select between `Italian`, `French`, and `Spanish` languages. Not only that, but you can also have the summary translated into your preferred language for better understanding."
)
option = st.selectbox(
    "Which language would you like it to be translated?",
    ("French", "Italian", "Spanish"),
)
st.button("DOWNLOAD TRANSLATION")

st.divider()

# --------------------------------------- Quiz generator -----------------------------------------#
st.header("Quiz Generator Service")

st.markdown(
    "Have you studied the summary carefully? Great! That means you're ready, right? Now, let's ask our Hugging Face agent to generate some engaging multiple-choice questions for you! Get ready to put your knowledge to the test!"
)
st.markdown(
    "You have the freedom to choose the language in which you want to be examined! Simply select your desired language option. Additionally, you can specify the number of questions you would like in your requested exam. Tailor the examination experience according to your preferences!"
)

st.markdown(
    "Once the agent has gathered this information, it will utilize another specialized tool called `quiz_generator_tool` to generate the quiz for you. This tool is specifically designed to create dynamic and engaging quizzes based on your selected preferences. Sit back and let the quiz generation process unfold!"
)
st.markdown(
    "Just a friendly reminder, once you click on `Generate Exam`, all subsequent steps will be presented in your selected language. For instance, you will have the option to listen to the question in the language of your choice. Furthermore, the question text will be translated into your preferred language for seamless comprehension. Enjoy the convenience of experiencing the entire exam process in your own language!"
)

exam_language = st.selectbox(
    "Generate exam in: ",
    ("French", "Italian", "Spanish"),
)

number_of_questions = st.text_input("Number Of Questions:")
st.button("GENERATE QUIZ")
st.divider()
st.header("Generated Quiz")
st.button("GET MY SCORE")
