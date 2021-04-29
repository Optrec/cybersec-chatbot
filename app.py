from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter",logic_adapters=[{
     #    "chatterbot.logic.BestMatch",
   
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        
}])
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")


@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(english_bot.get_response(userText))
    #  return str(userText)

if __name__ == "__main__":
     app.run(debug = True, port=8000)


