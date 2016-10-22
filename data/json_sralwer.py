#!/usr/bin/python
# coding:utf-8

import requests
import json
import pymongo

ip = '127.0.0.1'
port = 27017
db_name = 'gd_map'
collection_name = 'pos_info'

# xiamen
url1 = 'http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&city=350200&geoobj=117.582876%7C24.33416%7C118.637564%7C24.646594&keywords=%E5%8E%A6%E9%97%A8%E5%B8%82'
#jimei
url2 = 'http://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&city=350200&geoobj=118.096307%7C24.575665%7C118.098367%7C24.576275&keywords=%E9%9B%86%E7%BE%8E%E5%8C%BA'

mongo_conn = pymongo.MongoClient(ip, port)
db = mongo_conn[db_name]
collection = db[collection_name]

for url in [url1, url2]:
    try:
        r = requests.get(url)
        j = json.loads(r.text)
        collection.save(j)
    except Exception as e:
        print e

