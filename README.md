This project is about sample chatbot to illustrate how NLP (Natural Language Processing) works.

How to Run project
1. Download or clone repository in your system 
2. Activate chatbot env before running any file
    --> chatbot\chatbot\Script\activate
3. Open all files in any python IDE
4. Run main.py file
   --> python main.py
5. Open browser and check host on which application is running
   --> http://127.0.0.1:5000/

Chatbot UI </br>
![image](https://github.com/vishnuSah/chatbot/assets/127580123/6dc6725b-1b5b-469d-a18d-25add19dea9a)


Summary:
This project is sample chat to illustrate how NLP (Natural Processing Language) technique works to understand user messages and provide appropriate responses. 
The chatbot is built using Python, NLTK and Flask for creating web interface.

STEPS: 
1. Data Prepation: </br>
  The project starts by defining intents in a JSON file (`intents.json`). Each intent has a unique name and contains two main components:
  examples: User mesages
  responses: Bot responses
2. User Input: </br>
When a user interacts with the chatbot's web interface, their input message is captured.
3. Intent Recognization Algorithm: </br>
The chatbot employs an intent recognition algorithm to determine the user's intent.
For each intent defined in `intents.json`, the chatbot checks if the user's input message contains any words or phrases that closely match the examples associated with that intent.
The chatbot can use techniques like keyword matching, fuzzy string matching, or even more advanced NLP approaches for better accuracy.
If the user's input closely matches the examples of a particular intent, that intent is recognized.
4. Response Generation: </br>
In (intents.json), each intent is associated with a list of possible responses. These responses are predefined and contextually relevant to the intention.
5. Random Response: </br>
From the list of possible responses for the recognized intent, the chatbot selects one response at random. This adds an element of unpredictability to the conversation, making it feel more natural.






