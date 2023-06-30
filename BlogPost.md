

AI/ML Transformer Tools Hackathon
Quizify: A self service study platform powered by Generative AI, using Hugging face Transformers.
The ` Self-Service Learning platform` is an innovative app designed to revolutionize your learning experience. With this powerful tool, users can effortlessly generate custom quizzes based on any PDF file they download from the web. Gone are the days of tedious manual summarization and translation! Our app leverages the cutting-edge capabilities of Hugging Face transformers to simplify the entire process. Once you've obtained a PDF, simply import it into the app and watch as the magic unfolds.

This learning platform empowers you to summarize the document with ease, condensing its key points into a concise format. Not only that, but our app also offers built-in translation functionality, allowing you to understand the content in your preferred language. But the true power of our app lies in its ability to transform your summarized and translated document into an interactive question-answer service.

By analyzing the text and extracting relevant information, the app generates thought-provoking questions that test your understanding of the material. Whether you're a student striving for academic excellence or a professional looking to enhance your knowledge, the Self Service Quiz Generator platform is your go-to tool for efficient and engaging learning.


Project Description

Project Title: Self Service Study Platform- Quizify

Quizify as the name implies is a simple service that leverages Hugging face transformer agents. Under the hood it runs custom tools to empower you to generate summaries for your documents, generate audio for your content, translate the summary to the language of your choice as well as generating questions to examine your understanding of the content.
This Tool can be used by students who need to summarize their content as well as parents who have to generate questions for their kids during exam time! No more hassle! 






Motivation


We are living in a very hectic era! Students are packed with so many study materials. Parents are so busy with all kind of works in their day to day life and need to consider they have covered enough to prepare their kids for their exam! Some people want to attend an exam but because of financial restrictions they can not invest much on exam materials. So this tool can be all in one for every group! 





Architectural Diagram







	



Process

During the initial stages of the project, our team engaged in brainstorming sessions to explore various ideas on how to leverage Transformers. We finally selected Darya's concept, the Language Whisperer, for our project. To facilitate collaborative development, Darya created a Google Colab notebook where team members could experiment and iterate on the initial codebase. As the project progressed, we transitioned to using GitHub, to streamline collaboration and ensure efficient code management among team members. This transition allowed for smoother coordination and enhanced teamwork throughout the development process. The following tools have been used:


StarCoder agent, an extensive language model (LLM), offers a natural language API built on top of transformers and has been employed for the purpose of implementation.  Detailed documentation for the agent can be found at the provided link  https://huggingface.co/docs/transformers/main_classes/agent .

Wiki Searcher (a custom tool) was implemented by utilizing BeautifulSoup, a Python library designed for extracting data from HTML and XML files. This library played a crucial role in parsing and navigating the HTML structure of web pages, enabling the extraction of relevant information for the Wiki Searcher application.

gTTS (Google Text-to-Speech) library (a custom tool) was used for converting text into high-quality speech output with natural-sounding voices. This decision stems from the observation that the default translator within the agent does not meet our desired level of effectiveness when it comes to accurately reading text in various languages. Amazon Polly was also tried for these purposes, but was hard manageable in terms of integration with Streamlit. 

Streamlit was used for the Frontend 


Challenges Faced
Finding the appropriate voice for the task proved to be quite challenging. Unfortunately, the built-in StarCoder text-to-speech tool rendered foreign phrases in English with a noticeable accent, causing confusion. Additionally, a decision was made to conduct research in order to find a suitable solution. One option considered was the utilization of Amazon Polly, although integrating it with streamlit presented difficulties, as it necessitated authorization to an AWS account. Alternatively, the gtts library offered a viable option, requiring no keys or access and easily installable via pip install. It simply required the addition of a language code as input, yielding natural-sounding voice output.

One of the challenges we encountered was determining the appropriate front-end stack for our machine learning application. Initially, we embarked on building a Next.js React application with Python APIs. However, in an effort to simplify the process, we made the decision to utilize Next.js embedded APIs instead of deploying lambda functions and an API gateway. Unfortunately, this decision led to significant issues due to dependencies. We found ourselves needing to containerize the Python library dependencies. Considering the urgency of implementing our idea as quickly as possible for a quick proof of concept, we altered our approach and opted to implement the user interface using Streamlit.

Lesson Learnt (New Skill Developed)
Use of Session States
Use of Amazon Polly
Use of Streamlit














Outcome

Within Quizify tool, you are empowered with multiple sub-services:

Step1: Downloader, Uploader Service

To begin, you have two options: either upload the file directly or provide a valid URL for your PDF resource.

If you choose to enter a URL, our advanced Hugging Face Agent will seamlessly download the file for you. This process utilizes a specialized tool known as the `download_file_tool` working silently behind the scenes to retrieve the document.

Currently, our platform exclusively supports PDF files at this stage.
As an alternative, you have the option to upload your PDF file. Our agent will utilize a specialized tool called `read_file_tool` to process and extract the content from the document. The extracted information will be saved for further use within the platform.
upload the image you would want to transcribe
select your preferred choice of language
play and listen to the transcribed language


Step2: Summarization Service
Let the fun begin! Get ready to dive into the exciting features of our app. How about downloading a summarization of your uploaded document or web content? Let's embark on this thrilling journey together!"

By clicking the `summarize` button below, the Hugging Face agent will generate a summary of your document. Please note that the summarization model used by the agent is the default tool, so the results may not be perfect. If your document is excessively large, there is a chance it may encounter difficulties or exhibit unexpected behavior while processing.

We haven't forgotten about that! You might be eager to download the summary, so go ahead and click the button to access it.

Step 3: Translation Service
Hmmm, perhaps English is your second language, just like mine! But don't worry, I've got your back 😉. With this tool, you can select between `Italian`, `French`, and `Spanish` languages. Not only that, but you can also have the summary translated into your preferred language for better understanding.

Step 4: Text-To-Speech Service

In addition to all we mentioned so far, if you are keen to listen to the summary or the original uploaded content, in this platform you will be able to generate audio from the file.

Step 5: Quiz Generator Service

Have you studied the summary carefully? Great! That means you're ready, right? Now, let's ask our Hugging Face agent to generate some engaging multiple-choice questions for you! Get ready to put your knowledge to the test!

You have the freedom to choose the language in which you want to be examined! Simply select your desired language option. Additionally, you can specify the number of questions you would like in your requested exam. Tailor the examination experience according to your preferences!
Once the agent has gathered this information, it will utilize another specialized tool called `quiz_generator_tool` to generate the quiz for you. This tool is specifically designed to create dynamic and engaging quizzes based on your selected preferences. Sit back and let the quiz generation process unfold



PROJECT OUTPUT

Github Repository: https://github.com/RonakReyhani/quizify ​​



Reflection


I have always harbored a deep passion for machine learning (ML), which makes every new concept or topic in the field incredibly enticing. Recently, my curiosity led me to explore the realm of Generative AI, specifically the renowned Hugging Face LLM models. Although I had heard about them in passing, I had never had the opportunity to delve into their intricacies. This project presented a remarkable chance to step out of my comfort zone and venture into the unknown.

Throughout this journey, I gained extensive knowledge about various aspects of the Hugging Face ecosystem, including Hugging Face Hub, models, transformers, pipelines, and the widely acclaimed "agent" that our app heavily relies on. Beyond the technical advancements, what truly made this experience exceptional was the opportunity to collaborate with an extraordinary team spanning across the globe. Through virtual meetings and vibrant discussions, we pooled our ideas and arrived at a common understanding. Working with them was truly inspiring, and their unwavering support allowed me the freedom to implement my ideas using the tools I was most comfortable with.

As the hackathon reached its conclusion, I not only acquired a wealth of knowledge about LLM models and Hugging Face agents, but I also forged incredible friendships. The prospect of meeting these newfound friends in person fills me with anticipation and excitement. In retrospect, this sense of camaraderie and connection stands as the greatest achievement of this endeavor.



FURTHER STEPS

Certainly this app can be extended and improved. This is just a proof of concept on how Hugging face models are efficient and how Agents can interact with different models of Hugging face Hub. How you can create a pipeline to transform the model and how to simply generate a custom tool from your functions.
Having a proper docker image which takes care of dependencies, and a nice and professional user interface will make this way more convenient and accessible to users. 
Another step I would like to take, is to retrain the text3text-generation model to create more professional exam questions such as AWS exam formats! 





