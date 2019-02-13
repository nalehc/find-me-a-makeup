from flask import Flask, request, render_template, abort, jsonify
import pickle
import random
import numpy as np
import os

app = Flask('__name__')

lsa_ = pickle.load(open('./dim_red.pkl', 'rb'))
count_vectorizer = pickle.load(open('./vectorizer.pkl', 'rb'))
nn = pickle.load(open('./model.pkl', 'rb'))

def get_nearest_prods(description):
    new_vec = lsa_.transform(count_vectorizer.transform([description]))
    results = nn.kneighbors(new_vec, n_neighbors=5)
    rec_strings = []
    for i in range(len(results[1][0])):
        rec_strings.append(f"Try {new_df.iloc[results[1][0][i]]['Name']}, a {new_df.iloc[results[1][0][i]]['Product']} by {new_df.iloc[results[1][0][i]]['Brand']}.")
    return rec_strings

@app.route('/')
def landing_page():
    greetings = ['Making makup wishes come true since 2019', 'Your wish is my command',
    'That floating feeling']
    greeting_choice = random.choice(greetings)
    return render_template("index.html", greeting_choice = greeting_choice)

@app.route('/predict', methods=['POST'])
def score_api():
    if not request.json:
        abort(400)
    response = make_prediction(request.json['data'])
    return jsonify(response), 201

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
