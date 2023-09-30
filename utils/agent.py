from chatbot import chatbot 

def agent(messege,hisory):
  bot=chatbot("your open ai key",0,"gpt-3.5-turbo-16k")
  response=bot.run(input=messege)
  return response