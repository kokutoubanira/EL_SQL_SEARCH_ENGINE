# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch

es = Elasticsearch("localhost:9200")

rq = {
    "query" : {
        "match": {
            "content": "ในใใ"
        }
    }
}

result = es.search(index="imdtable", body=rq)
print(result)