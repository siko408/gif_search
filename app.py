from flask import Flask, render_template, request
from random import randint
import requests
import json
import os

app = Flask(__name__)

'''
# TODO: Extract query term from url
search_term = "dog"
search_term = request.args.get("search_term")
# TODO: Make 'params' dict with query term and API key
params = {"api_key": "LIVDSRZULELA", "query": search_term}
# TODO: Make an API call to Tenor using the 'requests' library
request_gifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["query"], params["api_key"], 10))
# TODO: Get the first 10 results from the search results
'''


@app.route('/')
def index():
    """Return homepage."""
    search_term = request.args.get("search_term")
    random_term = request.args.get("random_term")

    if(random_term is not None):
        search_term = rand_word()
        params = {"api_key": "LIVDSRZULELA", "query": search_term, "limit": 10}
    elif(search_term is None):
        params = {"api_key": "LIVDSRZULELA", "query": "", "limit": 10}
    else:
        params = {"api_key": "LIVDSRZULELA", "query": search_term, "limit": 10}

    try:
        request_gifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["query"], params["api_key"], params["limit"]))
    except Exception:
        return render_template("error.html")

    if request_gifs.status_code == 200:
        try:
            gifs = json.loads(request_gifs.content)

        except Exception:
            print("Error passing json file")

    elif request_gifs.status_code == 404:
        return render_template("error.html")

    else:
        gifs = None

    gifs = gifs["results"]
    return render_template("index.html", gifs=gifs, search_term=search_term)


def filter(word):
    """
    This function removes all '/n' from a text line
    """
    x = word[0:len(word) - 1]
    return x


def rand_word():
    count = 0
    word_file = open("words.txt", "r")
    line = word_file.readlines()
    for x in line:
        count += 1
    random_limit = len(line) - 1
    search_term = filter(line[randint(1, random_limit)])
    return search_term


if __name__ == '__main__':
    app.run(debug=True)
