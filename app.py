from flask import Flask, render_template, request
from random import randint
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():

    """
    This is the homepage. It extracts the search term that was supplied by
    the user or if they chose to generate a random term it calls rand_word().
    """
    search_term = request.args.get("search_term")
    random_term = request.args.get("random_term")

    if(random_term is not None):
        try:
            search_term = rand_word()

        except Exception:
            return render_template("error.html")
        params = {"api_key": "LIVDSRZULELA", "query": search_term, "limit": 10}

    elif(search_term is None):
        params = {"api_key": "LIVDSRZULELA", "query": "", "limit": 10}

    else:
        params = {"api_key": "LIVDSRZULELA", "query": search_term, "limit": 10}

    """
    After determining what the search_term is then we request it from
    https://api.tenor.com
    """
    try:
        request_gifs = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
            (params["query"], params["api_key"], params["limit"]))

    except Exception:
        return render_template("error.html")

    """
    Then we extract the json data from our request.
    """
    if request_gifs.status_code == 200:
        try:
            gifs = json.loads(request_gifs.content)

        except Exception:
            render_template("error.html")

    elif request_gifs.status_code == 404:
        return render_template("error.html")

    else:
        gifs = None

    """
    After extracting the data from the json file we pare it down to just what
    is in the results dictionary entry.
    """
    gifs = gifs["results"]

    """
    Then we render our index.html template and pass our gifs and the last
    searched term so that we can display them later.
    """
    return render_template("index.html", gifs=gifs, search_term=search_term)


def rand_word():
    """
    This funtion should return a random word from the words.txt file.
    It might be called from the index() function if the user asks for a random
    search term.
    """
    word_file = open("words.txt", "r")
    line = word_file.readlines()
    random_limit = len(line) - 1
    search_term = filter(line[randint(1, random_limit)])
    return search_term


def filter(word):
    """
    This function removes all '/n' from a text line
    """
    x = word[0:len(word) - 1]
    return x


if __name__ == '__main__':
    app.run(debug=True)
