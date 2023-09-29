from chatbot import chatbot 

def agent(messege,hisory):
  bot=chatbot("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",0,"gpt-3.5-turbo-16k")
  response=bot.run(input=messege)
  return response