import os
import openai
# Create instance of FieldStorage 
# Get data from fields

class TextPredictor():
  def __init__(self):
    self.prompts = "Decide what Human Right Article is associated with the description text.\n\nDescription: Housing Demolition\nHuman Rights Article: Article 25\n\nDescription: Restricted Speech\nHuman Rights Article: Article 19\n\nDescription: unfair hearing\nHuman Rights Article:  Article 14 \n\nDescription: torture\nHuman Rights Article: Article 5\n\nDescription: I was imprisoned unfairly by the government\nHuman Rights Article:  Article 9\n\nDescription: The government demolished my home and is refusing to give me health treatment.\nHuman Rights Article:  Article 25 and Article 12"
    self.model = "text-davinci-002"
    self.key = "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"
    self.answer = None
    openai.api_key = "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"
  def update_prompt_answer(self, answer):
    self.prompts += answer
    return 
  def description_update_prompt(self, description):
    self.prompts += "\n\nDescription: "+description+"\nHuman Rights Article: "
    return 
  def article_prediction(self):
    return self.answer
  def api_request(self):
    self.answer = openai.Completion.create(
    model="text-davinci-002",
    prompt=self.prompts,
    temperature=0.1,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0)
    self.answer = self.answer['choices'][0]['text']
    return

  def request(self, description):
    self.description_update_prompt(description)
    self.api_request()
    self.update_prompt_answer(self.answer)
    return 

if __name__=="__main__":
  bot_reader = TextPredictor()
  descrp = "I am not treated as an equal."
  bot_reader.request(descrp)
  article_prediction = bot_reader.article_prediction()

  print(descrp, article_prediction)

