from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    # serch_term = request.args.get("search_term")
    # TODO: Make 'params' dict with query term and API key
    params = {"api_key": "LIVDSRZULELA", "query": request.args.get("search_term")}
    # TODO: Make an API call to Tenor using the 'requests' library
    request_gifs = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params["api_key"], params["query"], 10))
    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
