from flask import Flask, render_template, request
from random import randint
from string import punctuation
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
    temp = False
    """Return homepage."""
    lmt = 10
    search_term = request.args.get("search_term")
    if(search_term is None):
        '''
        count = 0
        word_file = open("words.txt", "r") #Ask why readlines must be underneath open file
        line = word_file.readlines()
        for x in line:
            count += 1
        try:
            random_limit = len(line) - 1
            of_word = filter(line[randint(1, random_limit)])
            params = {"api_key": "LIVDSRZULELA", "query": of_word}
            temp = True
        except:
            of_word = search_term
            print("An error occured")
        '''
        params = {"api_key": "LIVDSRZULELA", "query": ""}

    else:
        params = {"api_key": "LIVDSRZULELA", "query": search_term}

    try:
        request_gifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["query"], params["api_key"], lmt))
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
    if(temp is not True):
        of_word = search_term
    print("Condition:", of_word)
    return render_template("index.html", gifs=gifs, search_term=search_term)


def filter(word):
    """
    This function removes all
    '/n' from a text line
    """
    x = word[0:len(word) - 1]
    return x


if __name__ == '__main__':
    app.run(debug=True, port=7000)
