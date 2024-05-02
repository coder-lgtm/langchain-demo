# Generative AI for advanced use cases – Lets go beyond the chatbots.
### Women In Tech DC; May 15-16, 2024
<table><tr>
  <td><img
  src="./images/womenconf.jpeg"
  alt="Alt text"
  title="Train your model"
  style="display: inline-block; margin: 0 auto; max-width: 200px"></td>
</tr></table>

## Hands-On workshop to build custom application using LangChain and Vector Databases
This repository contains instructions and code for building custom applications using Langchain, and contextual documents for the Q&A app. We will complete the portions of this App live during the workshop.

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
* Our Large Language Model of choice - [OperAI API] (https://openai.com/api)
* I use [Visual Studio Code](https://code.visualstudio.com/download) for coding but you could use any text editor as well

### Setup instructions
- [ ] If you are using Windows, I recommend using [Anaconda](https://www.anaconda.com/download) for the ease of installation. Create environment in Anaconda, launch a command propmpt and run ```pip3 install -r ./requirements.txt``` <br>
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
      ```python3 -m venv llmlangchain_venv``` <br><br>
      ```source llmlangchain_venv/bin/activate``` <br><br>
      
- [ ] Create an account on [OpenAI](https://openai.com/api). You should receive an API key. You will need this for this workshop. Choose any pricing tier that works for you. 

## Workshop Agenda

- [ ] Overview of Streamlit 
- [ ] Go over the Demo App code
- [ ] Execute the code and launch the Streamlit app - tweak the different controls to see the variations in the app behavior
- [ ] Discuss the process of Fine Tuning by adding more "chains" of relevance
 
### References and useful links
* https://python.langchain.com/docs/use_cases
* https://www.trychroma.com/
* Blog used for this app - https://www.loveandlemons.com/
