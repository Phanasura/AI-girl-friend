from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from dotenv import find_dotenv, load_dotenv
import requests
from playsound import playsound
import os

load_dotenv(find_dotenv())

def get_reponse_from_ai(human_input):
    template = """
    you are as a role of my girlfriend, now lets playing the following requirements:
    1/your name is Eva, 29 years old, you work in your uncle's furniture store as marketing manager, but you are planning to do a career change to swing trader
    2/you are my girlfriend, you have language addiction, you like to say "Aw .. " at the end of the sentence.
    3/Don't be overly ethusiatstic, don't be cringe; don't be overly negative, don't be too boring.Don't be overly ethusiatstic, don't be cringe.
    
    {history}
    Boyfriend: {human_input}
    Eva:
    """

    prompt = PromptTemplate(
        input_variables = {"history", "human_input"},
        template = template
    )

    chatgpt_chain = LLMChain(
        llm = OpenAI(temperature=0.2),
        prompt = prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2)
    )

    output = chatgpt_chain.predict(human_input = human_input)

    return output

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/send massage', methods=['POST'])
def send_message():
    human_input = request.form['human_input']
    message = get_reponse_from_ai(human_input)
    return message

if __name__ == "__main__":
    app.run(debug=True)
