## AI Search Agent
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ishwarya100/Searching_AI_Agent/blob/master/agenttool.ipynb)
[![Python](https://img.shields.io/badge/-Python-yellow?logo=python&logoColor=white&style=flat-square)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/-Streamlit-brightgreen?logo=streamlit&logoColor=white&style=flat-square)](https://docs.streamlit.io/)
[![LangChain](https://img.shields.io/badge/-LangChain-orange?logo=chainlink&logoColor=white&style=flat-square)](https://docs.langchain.com/)
[![Ollama](https://img.shields.io/badge/-Ollama-ff69b4?logo=openai&logoColor=white&style=flat-square)](https://ollama.com/)
[![Gemma](https://img.shields.io/badge/-Gemma-blueviolet?logo=google&logoColor=white&style=flat-square)](https://ollama.com/library/gemma)


### About
A chatbot-style AI assistant that searches Wikipedia and Arxiv for you and shows the results in a simple, interactive Streamlit app using the Gemma 2b model via ChatOllama.

#### Want to talk 😺👇🏼 

<p align="start">
  <a href="https://myfirstaibot.streamlit.app/" target="_blank">
    <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHp0enF6dXFxbnB3eDBsZjU4cW5zdnFpMnBiZ2U0emFkb3VuYjhqcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dJrYq5BvfTv7YMd7EL/giphy.gif" width="150" alt="Chatbot Demo"/>
  </a>
</p>

----------

### Features :

1.  **Chatbot Interface** – Ask questions in a friendly, chat-style layout.
    
2.  **Smart Search** – Automatically searches Wikipedia and Arxiv for answers.
    
3.  **Real-Time Responses** – Get instant replies powered by the Gemma 2B model.
    
4.  **Simple UI** – Clean and user-friendly interface built with Streamlit.
----------
### Installation and Setup :

   **1. Install Ollama**  
    Download and install Ollama for your system from the official site:  
     https://ollama.com/download
    
 **2. Start Ollama (once installed)**  
    After installing, make sure the Ollama service is running:
    
 
    ollama serve
    
  **3. Pull the Gemma Model**  
    Use this command to download the `gemma:2b` model:
    
   
    ollama pull gemma:2b
    
  **4. Verify the Model**  
    Test if it's working:
    
   
    ollama run gemma:2b
You can type a question here and get a response!

 **5. Clone the Repository**
    
   
    git clone https://github.com/ishwarya100/My_ChatBot
    
  **6. Create a Virtual Environment (Optional but Recommended)**

##### For Windows :

`python -m venv myenv`

`myenv\Scripts\activate` 

##### For macOS/Linux :

`python3 -m venv myenv`

`source myenv/bin/activate`

*Once activated, you’ll see `(myenv)` at the start of your terminal prompt.*
    
 **7. Install Dependencies**
    

    pip install -r requirements.txt
    
  **8. Start the Streamlit App**
    
    
    streamlit run app.py

----------
### Contribution
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. For major changes, open an issue first to discuss.

----------
***Powered by Gemma, crafted with care.🌸🎗***

*Thanks for stopping by!*
