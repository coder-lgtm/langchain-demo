# Generative AI for advanced use cases – Lets go beyond the chatbots
### Women In Tech DC; May 15-16, 2024
<table><tr>
  <td><img
  src="./images/womenconf.jpeg"
  alt="Alt text"
  title="Train your model"
  style="display: inline-block; margin: 0 auto; max-width: 200px"></td>
</tr></table>

## Hands-On workshop to build a custom application using LangChain, RAG and Vector Databases
This repository contains instructions and code for building a custom application using Langchain, and contextual documents for the Q&A app. We will complete the portions of this App live during this workshop.

### What are we building?
A Q and A app that can share recipes with you from two books that we have downloaded from the internet. Then, you would be able to create YouTube video script using the traditional LLM as the second chain of operations.

### Goals
* Review core LLM concepts
* Get familiarized with advanced concepts surrounding Generative AI
* Overview of LangChain and Vector Databases
* Overview of RAG (Retrieval Augmented Generation) 
* Build an app using a OpenAPI apis, LangChain python library and Vector Database
  
### Repository contains
* Setup instructions for the Open Source technologies for this workshop
* Code to build Q&A Python Application using LangChain, RAG and Vector Database
  
## Pre-workshop setup steps
### We will be using following tools and resources
* Our choice of programming language -  [Python 3.8](https://www.python.org/downloads/release/python-380/)
* Quick and elegant app builder - [Streamlit](https://streamlit.io/)
* Langchain Open Source Python Library - [LangChain](https://python.langchain.com/docs/get_started/introduction/)
* Our Large Language Model of choice - [OperAI API] (https://openai.com/api)
* Vector Database - [Chroma DB] (https://www.trychroma.com/)
* I use [Visual Studio Code](https://code.visualstudio.com/download) for coding but you could use any text editor as well

### Setup instructions
- [ ] If you are using Windows, I recommend using [Anaconda](https://www.anaconda.com/download) for the ease of installation. Create environment in Anaconda, launch a command propmpt and run ```pip3 install -r ./app/requirements.txt``` <br>
- [ ] For Mac, Install Homebrew if you don't have it. <br>
      Go to a terminal and run ```$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```
- [ ] Install python 3.8 using homebrew <br>
      ```brew install python@3.8```
      
- [ ] Checkout this repository </br>
      ```git clone git@github.com:coder-lgtm/langchain-demo.git``` <br> (You will need to have SSH key setup for this) <br><br>
      OR <br>
      ```git clone https://github.com/coder-lgtm/llm-demo.git``` <br> (You do not need SSH key for setup for this)  <br><br>
      OR <br>
      Just download the repository from https://github.com/coder-lgtm/langchain-demo/archive/refs/heads/main.zip and unzip <br>
- [ ] Navigate to langchain-demo/app directory and run the following to install dependencies using the requirements.txt <br>
      If you want to run this app locally, you will need to install streamlit, langchain and other packages. Following virtual environment will do 
      just that. <br>
      ```cd langchain-demo``` <br><br>
      ```python -m venv env``` <br><br>
      ```source ./env/bin/activate``` <br><br>
      ```pip install -r ./app/requirements.txt``` <br><br>
- [ ] Create an account on [OpenAI](https://openai.com/api). You should receive an API key. You will need this for this workshop. Choose any pricing tier that works for you. 

## Workshop Agenda

- [ ] Overview of Streamlit 
- [ ] Build the App step by step
- [ ] Execute the code and launch the Streamlit app - tweak different controls to see the variations in the app behavior
- [ ] Discuss the process of Fine Tuning by adding more "chains" of relevance
 
### References and useful links
* https://python.langchain.com/docs/use_cases
* https://www.trychroma.com/
* Two free Recipe books that I downloaded and added to ./docs directory
  
