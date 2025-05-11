# YouTube QA Chatbot

This repository contains a simple **YouTube Question Answering (QA) Chatbot** that answers questions based on a given text file containing a list of sentences. The chatbot uses the **Sentence-Transformers** model (`all-MiniLM-L6-v2`) to provide context-based answers to user queries.

## Features
- **Single-chat conversation**: Ask a question, and the bot will return an answer based on the content in a provided text file.
- **Customizable**: You can update the text file with your own data and questions.
- **Pre-trained Model**: Uses the `all-MiniLM-L6-v2` model for efficient sentence embeddings and similarity comparison.
- **No history tracking**: This version supports only single question-answer interactions.

## Requirements

Before running the chatbot, ensure that you have the following installed:

- Python 3.6+
- `faiss-cpu` (for efficient similarity search)
- `sentence-transformers` (to encode questions and sentences)

### Install Dependencies

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/SachinduNethmina/qachatbot

2. Create a virtual environment (optional but recommended for isolating dependencies):
   ```bash
   python -m venv .venv

3. Activate the virtual environment:
   - Windows:
      ```bash
      .venv\Scripts\activate
   - macOS/Linux:
      ```bash
      source .venv/bin/activate

4. Install the required dependencies from `qachatbot/requirements.txt`:
   ```bash
   pip install -r qachatbot/requirements.txt

### How to Use

1. Prepare Your Data:
   Edit the `qachatbot/sentences.txt` file or create your custom text file to include the text that the bot will use to answer questions. This can be any data related to a general FAQ document.

   Example content for `sentences.txt`:
   ```text
   YouTube is a video-sharing platform that allows users to upload, view, and share videos.
   The platform was created by three former PayPal employees: Chad Hurley, Steve Chen, and Jawed Karim in February 2005.
   YouTube allows users to upload videos in various formats, including MP4, MOV, and AVI.
   YouTube's algorithm recommends videos based on the user's watch history and preferences.

2. Run the Chatbot:
   Once everything is set up, you can interact with the bot by running the your main script.

   Here is an example of how you can use the bot in example main.py:
   ```python
   from qachatbot.bot import QAChatBot

   def main():
       # Create an instance of the chatbot
       bot = QAChatBot()

       # Load the sentences from the text file
       bot.load_sentences('qachatbot/sentences.txt')

       # Ask a question and get the response
       question = "What is youtube?"
       print("User:", question)
       print("Bot:", bot.ask_question(question))

   if __name__ == "__main__":
       main()

3. Running the Script:
   To interact with the bot, simply run the following command in your terminal:
   ```bash
   python main.py

You will see an output like this:
   
User: What is youtube?
Bot: YouTube is a video-sharing platform that allows users to upload, view, and share videos.
