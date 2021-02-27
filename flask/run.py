import os
import sys
import json
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def displayapp():
    data = np.load("data/tsne.npy")
    json_data = []
    with open('data/filenames.txt', 'r') as f:
        for i, item in enumerate(f):
            json_data.append({"x": np.asscalar(data[i, 0]),
                              "y": np.asscalar(data[i, 1]),
                              "filename": item.strip('\n')})
    # print(json_data)
    return render_template("index.html", img_dict=json_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)