import os
from pprint import pprint
from flask import Flask, render_template, jsonify, request
from elasticsearch import Elasticsearch

# Elasticsearchにインデクシング
es = Elasticsearch("http://localhost:9200/")
from collections import defaultdict


body_ngram = {
    "query" : {
        "match" : {
            "content": {
            "query": "ライダー オーズ",
            "operator": "and",
            "fuzziness" : "AUTO",
            "prefix_length" : 1,
            "boost": 1.3
            }
        }
    },
    "_source" : ["_score", "id", "content"],
    "from": 0,
    "size": 1000
}

res = es.search(index="imdtablema", body=body_ngram)
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

body_ma = {
    "query" : {
        "match" : {
            "content": {
            "query": "ライダー オーズ",
            "operator": "and",
            "fuzziness" : "AUTO",
            "prefix_length" : 1
            }
        }
    },
    "_source" : ["_score", "id", "content"],
    "from": 0,
    "size": 1000
}

res = es.search(index="imdtablengram", body=body_ma)
for hit in res['hits']['hits']:
    if hit['_source']['id'] in id_list.keys():
        tmp_list[id_list[hit['_source']['id']]]["score"] = tmp_list[id_list[hit['_source']['id']]]["score"] + hit['_score']
    else :
        s_dict = {}
        s_dict["id"] = hit['_source']['id']
        s_dict["score"] = hit['_score']
        s_dict["content"] = hit['_source']['content']
        id_list[hit['_source']['id']] = count
        count += 1
        tmp_list.append(s_dict)
import json

print(json.dumps(sorted(tmp_list, key=lambda x: x['score'], reverse=True), indent=2, ensure_ascii=False))