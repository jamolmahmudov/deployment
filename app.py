from flask import Flask , request
import telegram

app = Flask(__name__)

TOKEN = '6904974035:AAFjfkFsHnygmw12JS4CdQFcjxUHvWwy624'

bot = telegram.Bot(TOKEN)
chat_id = '6897251542'

@app.route('/', methods = ["POST"])

def main():
    data = request.get_json()
    print(data)
    bot.send_message(chat_id=data.message.chat.id,text=data.message.text)
    

if __name__=="__main__":
    app.run(debug=True, port=7000)