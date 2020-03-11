from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot  = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route('/get')
def get_bot():
    print(request.args.get('msg'))
    userText = request.args.get('msg')
    print(english_bot.get_response(userText))
    return str(english_bot.get_response(userText))

if __name__ == "__main__": 
    app.run()