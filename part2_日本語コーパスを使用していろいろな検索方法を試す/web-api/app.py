import os
from pprint import pprint

from flask import Flask, render_template, jsonify, request
from elasticsearch import Elasticsearch
import json

SEARCH_SIZE = 100

app = Flask(__name__)

es = Elasticsearch('elasticsearch:9200')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def analyzer():
    query = request.args.get('q')

    body = {
        "query" : {
            "function_score": {
            "query": {
                "bool": {"should": [
                {"match": {"content_ma": {
                    "query": "オーズ",
                    "boost": 0.5
                }}},
                {"match": {"content": {
                    "query": "ライダー オーズ",
                    "boost": 2
                }}}
                ]}
            }
            }
        },
        "_source" : ["_score", "id", "content"],
        "from": 0,
        "size": 1000
    }

    res = es.search(index="imdtable", body=body)
    tmp_list = []
    id_list = {}
    count = 0
    for hit in res['hits']['hits']:
        s_dict = {}
        s_dict["id"] = hit['_source']['id']
        s_dict["score"] = hit['_score']
        s_dict["content"] = hit['_source']['content']
        id_list[hit['_source']['id']] = count
        count += 1
        tmp_list.append(s_dict)
    print(query)
    return jsonify({"hits":sorted(tmp_list, key=lambda x: x['score'], reverse=True)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)