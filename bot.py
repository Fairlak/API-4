import telegram

bot = telegram.Bot(token='2003207826:AAGwbTHyKGjAhFfcCQSQJSmukRlE4ggr1Ls')

bot.send_message(chat_id=-1001428777443, text="-_- pablo")

bot.send_document(chat_id=-1001428777443, document=open('images/spacex0.jpg', 'rb'))