from flask import Flask, render_template, request
from main import TextPredictor
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    answer = 'The Articles of Human Rights associated with your report will appear here.'
    if request.method == "POST":
        description_to_classify = request.form.get("user_description")

        bot_reader = TextPredictor()
        bot_reader.request(description_to_classify)
        article_prediction = bot_reader.article_prediction()

        return render_template('./index.html', display_request = article_mapper(article_prediction), article = article_prediction )
    else:    
        return render_template('./index.html', display_request = answer)
def article_mapper(article_name):
    df = pd.read_csv('human_rights_articles.csv')
    df.set_index("Article Name", inplace=True)
    if not article_name.strip().__contains__('Article'):
        return 'This is not a human rights issue.'
    else:    
        return df.loc[str(article_name.strip())][0]

# app.run(host='0.0.0.0', port=8080)
if __name__ == '__main__':
    app.run()