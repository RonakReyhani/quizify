# quizify

A self service study platform powered by Generative AI, using Hugging face Transformers.

## Introduction

The ` Self-Service Learning platform` can be converted to an innovative app designed to revolutionize your learning experience. With this powerful tool, users can effortlessly generate custom quizzes based on any PDF file they download from the web. Gone are the days of tedious manual summarization and translation! this potential application leverages the cutting-edge capabilities of Hugging Face transformers to simplify the entire process. Once you've obtained a PDF, simply import it into the app and watch as the magic unfolds.

This learning platform empowers you to summarize the document with ease, condensing its key points into a concise format. Not only that, but our app also offers built-in translation functionality, allowing you to understand the content in your preferred language. But the true power of our app lies in its ability to transform your summarized and translated document into an interactive question-answer service.

By analyzing the text and extracting relevant information, the app generates thought-provoking questions that test your understanding of the material. Whether you're a student striving for academic excellence or a professional looking to enhance your knowledge, the Self Service Quiz Generator platform is your go-to tool for efficient and engaging learning.

As students, parents, or job seekers, we often encounter situations where we need to summarize a document promptly and prepare questions for ourselves or our children. This inspired the concept of a self-service platform. The platform allows users to upload documents or retrieve files from the internet, enabling them to summarize the content, translate it into their preferred language, and even generate questions based on the document.

## Sub Services

### Downloader, Uploader Service

To begin, you have two options: either upload the file directly or provide a valid URL for your PDF resource.

If you choose to enter a URL, our advanced Hugging Face Agent will seamlessly download the file for you. This process utilizes a specialized tool known as the `download_file_tool` working silently behind the scenes to retrieve the document.

Currently, our platform exclusively supports PDF files at this stage.
As an alternative, you have the option to upload your PDF file. Our agent will utilize a specialized tool called `read_file_tool` to process and extract the content from the document. The extracted information will be saved for further use within the platform.

### Summarization Service

let the fun begin! Get ready to dive into the exciting features of our app. How about downloading a summarization of your uploaded document or web content? Let's embark on this thrilling journey together!"

By clicking the `file_summarization_tool` button below, the Hugging Face agent will generate a summary of your document. Please note that the summarization model used by the agent is the default tool, so the results may not be perfect. If your document is excessively large, there is a chance it may encounter difficulties or exhibit unexpected behavior while processing.

We haven't forgotten about that! You might be eager to download the summary, so go ahead and click the button to access it.

### Translation Service

Hmmm, perhaps English is your second language, just like mine! But don't worry, I've got your back 😉. With this tool, you can select between `Italian`, `French`, and `Spanish` languages. Not only that, but you can also have the summary translated into your preferred language for better understanding.

### Text-To-Speech Service

In addition to all we mentioned so far, if you are keen to listen to the summary or the original uploaded content, in this platform you will be able to generate audio from the file.

### Quiz Generator Service

Have you studied the summary carefully? Great! That means you're ready, right? Now, let's ask our Hugging Face agent to generate some engaging multiple-choice questions for you! Get ready to put your knowledge to the test!

You have the freedom to choose the language in which you want to be examined! Simply select your desired language option. Additionally, you can specify the number of questions you would like in your requested exam. Tailor the examination experience according to your preferences!
Once the agent has gathered this information, it will utilize another specialized tool called `quiz_generator_tool` to generate the quiz for you. This tool is specifically designed to create dynamic and engaging quizzes based on your selected preferences. Sit back and let the quiz generation process unfold!
