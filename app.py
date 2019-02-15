from flask import Flask, request, render_template, abort, jsonify
import pickle
import random
import numpy as np
import os
import pandas as pd

app = Flask('__name__')

lsa_ = pickle.load(open('./dim_red.pkl', 'rb'))
count_vectorizer = pickle.load(open('./vectorizer.pkl', 'rb'))
nn = pickle.load(open('./model.pkl', 'rb'))
new_df = pickle.load(open('./reviews.pkl', 'rb'))

def get_nearest_prods(description):
    new_vec = lsa_.transform(count_vectorizer.transform([description['description']]))
    results = nn.kneighbors(new_vec, n_neighbors=5)
    rec_strings = []
    for i in range(len(results[1][0])):
        rec_strings.append(f"Try {new_df.iloc[results[1][0][i]]['Name']}, a {new_df.iloc[results[1][0][i]]['Product']} by {new_df.iloc[results[1][0][i]]['Brand']}.")
    return rec_strings

@app.route('/')
def landing_page():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def score_api():
    if not request.json:
        abort(400)
    response = get_nearest_prods(request.json['data'])
    return jsonify(response), 201

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
