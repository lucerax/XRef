import json
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, url_for
from getKeys import keyResult
from bing import bingResult
import requests
import os
import logging
from bs4 import BeautifulSoup


app = Flask(__name__)
CORS(app)


masterDic = {}

"""
@app.route('/get', methods = ['GET'])
def returnDic():
    return jsonify(masterDic)
"""


@app.route('/send_url', methods = ['GET', 'POST'])
def send_url():
    link = request.get_json()['u'] #args.get('u')
    data = {"returned_url": link}
    #print(request.args)
    #print(link)
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    #print('souped')
    #filter html for relevant text
    txt = [x.get_text() for x in soup.find_all('div', {'class':'zn-body__paragraph speakable'})]
    #print("txt: ", txt)
    #print('HERE IS OUTPUT')
    article = " ".join(txt)
    #print(article)
    #print(article)
    #return type must be json for Flask
    keywords = keyResult(article) #going from article to keywords
    #print(keywords)
    newsInfo = bingResult(keywords) #going from keywords to related news
    ###newsInfo = {"title": [], "provider": [], "description": []}###
    def set_default(obj):
        if isinstance(obj, set):
            return list(obj)
        raise TypeError
    #newsString = json.dumps(news, default=set_default);
    return jsonify(newsInfo) #displaying informations about related news


@app.route("/")
def index():
    return render_template("index.html")
# #reroute to index.html
# @app.route('/', methods = ['GET'], defaults = {'path':'index.html'})
# @app.route('/<path:path>', methods = ['GET'])
# def static_file(path):
#     #adds path to end of static
#     return send_from_directory('static', path)



if __name__== "__main__":
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.INFO)
    app.run(debug=True)
