# -*- coding: utf-8 -*-
"""
@author: Samuel Rocha
"""

# Importacion de archivos x
import json
import html
import pandas as pd
from pymongo import MongoClient, GEO2D

#si se deja por default el puerto en local esta es la dirección
conn = MongoClient("mongodb://127.0.0.1:27017/")
db = conn.ageb_social_good
col_ageb = db.ageb

def get_ageb(colection, latitude,longitude):
    try:
        ageb = colection.find_one({ "geometry": { "$geoIntersects": { "$geometry": { "type": "Point", "coordinates": [ longitude , latitude ] } } } })    
        return [ageb.get('properties').get('cvegeoedo'),
                ageb.get('properties').get('cve_mun'),
                ageb.get('properties').get('cvegeoageb')
                ]
    except:
        return ""

LAT = 19.4910202
LON = -99.1242766

ageb = get_ageb(col_ageb, LAT,LON)

print (" estado: ", ageb[0], " municipio ", ageb[1]," ageb: ",ageb[2])