from flask import Flask, request, render_template
from similarity_calculator import calc_similarity

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        text1 = request.form['text1']
        text2 = request.form['text2']
        similarity = calc_similarity(text1, text2)
        return render_template('result.html', result="{:.2f}".format(similarity*100))
    else:
        return render_template('index.html')

if __name__ == "__main__":
    print('hi')
    app.run(host="0.0.0.0")