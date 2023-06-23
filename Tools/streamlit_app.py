from huggingface_hub import login
from transformers import HfAgent
import pandas as pd
import streamlit as st
import downloader as downloader
import readPDF as fileReader

# manage secret
# Deployment
# summarizer
# exam generator
# show the multiple choice with pagination
# read the question for me
# generate score
# show my results
# chart for score after multiple times as a comparison on the same document.
# check how to create multi page app
# styling
# Deployment
# blog post
# Submit the form


# login to huggingface hub
token = st.secrets["hugging_face_token"]
login(token)

intoroduction = ""

tools = [downloader.download_file_tool,fileReader.read_file_tool]
agent = HfAgent("https://api-inference.huggingface.co/models/bigcode/starcoder",additional_tools=tools)
def download(url):
    return agent.run(f"Download file from the web {url}", url=url)

st.title("Self Service Quiz Generator platform")
st.divider()
st.header("Introduction")
st.markdown("the 'Self Service Quiz Generator platform' is an innovative app designed to revolutionize your learning experience. With this powerful tool, users can effortlessly generate custom quizzes based on any PDF file they download from the web.\nGone are the days of tedious manual summarization and translation! Our app leverages the cutting-edge capabilities of Hugging Face transformers to simplify the entire process. Once you've obtained a PDF, simply import it into the app and watch as the magic unfolds.\nThe Self Service Quiz Generator platform empowers you to summarize the document with ease, condensing its key points into a concise format. Not only that, but our app also offers built-in translation functionality, allowing you to understand the content in your preferred language.\n But the true power of our app lies in its ability to transform your summarized and translated document into an interactive multi-choice quiz. By analyzing the text and extracting relevant information, the app generates thought-provoking questions that test your understanding of the material.\n Whether you're a student striving for academic excellence or a professional looking to enhance your knowledge, the Self Service Quiz Generator platform is your go-to tool for efficient and engaging learning. Experience the convenience, accuracy, and effectiveness of our app today and take your learning journey to new heights.")
st.divider()
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
def set_clicked():
    st.session_state.clicked = True

# Enter URL or upload file
st.header("Downloader, Uploader Service")
st.markdown("To get started, you either need to upload the file or provide a valid url for your pdf resource.")
st.markdown("In this step, if you enter a URL Hugging Face Agent behind the scene will download the file. download file is a custom tool called `download_file_tool`.")
url = st.empty()
url = st.text_input('Enter a valid URL:')


col1, col2, col3, col4 = st.columns([0.4,0.2, 0.3, 0.3])
with col1:
   pass
with col2:
   pass
with col3:
    # to do: add a downloader for file name with button
    btn = st.download_button(
            label="DOWNLOAD FILE",
            data="file",
            file_name="url",
            mime="text/pdf"
        )
with col4:
   button =st.button("USE WEB CONTENT",on_click=set_clicked)
   if url and button and st.session_state.clicked:
        download(url)

st.markdown("Alternatively, You can choose to upload your pdf file, the agent will read the document with a custom tool called `read_file_tool` and saves the file.")
#  On file Upload
uploaded_file = st.file_uploader("Choose a file", type=['pdf'])
if uploaded_file is not None:
    # # To read file as bytes:
    bytes_data = uploaded_file.read()
    file_name = uploaded_file.name
    with open(file_name, 'wb') as f:
        f.write(bytes_data)
st.divider()

st.header("Summarization Service")
st.markdown("And now, the fun gets started! How about downloading a summarization on your uploaded document or the web content? lets get started.")

st.markdown("On click `summarize` button bellow, the Hugging face agent will summarize your document. The summarization model is the agent default tool. so please do not expect too much! yeah if your document is too large, it might behave funny and give up on reading!")
st.button("SUMMARIZE")
st.markdown("And hey! I have not forgotten about that, yeah you might want to download the summary. so go ahead and click the button.")
st.button("DOWNLOAD SUMMARY")
st.divider()
st.markdown("Hmmm, Maybe like me, English is your second language? don't worry I have gotten your back ;). With this tool you can between `Italian`, `French` and `Spanish` languages and the the summary translated to your language")

option = st.selectbox(
    "Which language would you like it to be translated?",
    ("French", "Italian", "Spanish"),
)
st.button("DOWNLOAD TRANSLATION")

st.divider()

st.header("Quiz Generator Service")

st.markdown("Did you study through? Ok! So that means you are ready hey? Let's ask our hugging face agent to generate some multiple choice questions for you!")
st.markdown("You can choose which Language you want to be examine against!, you can select the number of questions in your requested exam.")

st.markdown("Once the agent has these information, it would ask another custom tool called  `quiz_generator_tool` to generate the quiz for you.")
st.markdown("Just a reminder, once you click on generate exam, all the following steps would be presented in your selected language. for instance, you would be able to listen to the question in language of your choice. and obviously the question text is translated to your language.")

exam_language= st.selectbox(
    "Generate exam in: ",
    ("French", "Italian", "Spanish"),
)

number_of_questions = st.text_input('Number Of Questions:')
st.button("GENERATE QUIZ")
st.divider()
st.header("Generated Quiz")
st.button("GET MY SCORE")