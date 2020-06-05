# -*- coding: utf-8 -*-
"""
@author: Samuel Rocha
"""

# Importacion de archivos x
import json
import pprint
from pymongo import MongoClient, GEO2D


#para activar el local, debemos de teclear mongod --dbpath mongodb-data/db en la terminal o donde ete tu base
conn = MongoClient("mongodb://127.0.0.1:27017/")

db = conn.ageb_social_good
col_ageb = db.ageb

## CARGAR ARCHIVOS GEOJSON EN COLECCION MONGO
data_ageb = open("input/ageb_mx.geojson",encoding="utf8")
x_ageb = json.load(data_ageb)

## Inserta ageb a mongo
col_ageb.create_index([("geometry", "2dsphere")])
col_ageb.insert_many(x_ageb["features"])


