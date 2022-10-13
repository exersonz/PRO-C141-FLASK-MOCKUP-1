from flask import Flask, jsonify, request
import csv
all_articles = []

with open('articles.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:] #1: is for storing ALL the data staring form index 1 to the end

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-articles")
def get_article():
    return jsonify({
        'data': all_articles[0],
        'status': 'success'
    }), 201

#assuming the user liked the article so we are removing it from the list
@app.route("/liked-article", methods = ['POST'])
def liked_article():
    #getting the info at 0 index
    article = all_articles[0]
    all_movies = all_movies[1:]
    liked_article.append(article)

    return jsonify({
        'status': 'success'
    }), 201

#assuming the user didn't like the article so we are removing it from the list
@app.route("/unliked-article", methods = ['POST'])
def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)

    return jsonify({
        'status': 'sucess'
    }), 201

if __name__ == '__main__':
    app.run()