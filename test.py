import nvdbapi
import pandas as pd

from flask import Flask, request, render_template
from wtforms import Form, IntegerField, StringField, validators
import requests

def getSkred(veg, fylke):
    skredtype = {4198 : 'Stein', 4199: 'Jord/løsmasse', 5351: 'Is/stein', 4200: 'Snø', 4201: 'Is', 4202: 'Flomskred (vann+stein+jord)', 4203: 'Sørpeskred (vann+snø+stein)', 13103: 'Utglidning av veg'}
    s = nvdbapi.nvdbFagdata(445)
    s.addfilter_geo({'vegreferanse' : veg, 'fylke' : fylke})
    i = 0
    antallskred =  {}
    for i in skredtype[i][0]:
        antallskred[skredtype[]]
        i = i + 1


#print(data)


skred = nvdbapi.nvdbFagdata(445)
skred.addfilter_geo( { 'vegreferanse' : 'Fv241', 'fylke' : 14})
print(skred.egenskaper())
skred.addfilter_egenskap('2326=4198')


print(skred.statistikk())
ettskred = skred.nesteNvdbFagObjekt()
print(ettskred.egenskapverdi(2326))
print(ettskred.egenskapverdi(2324))
print(ettskred.egenskap(2326))
"""
i = 0
for i in range(0, 1):
    i = i + 1
    ettskred = skred.nesteNvdbFagObjekt()
    print(ettskred.egenskapverdi(2326))
    print(ettskred.egenskapverdi(2324))
    print(ettskred.egenskapverdi(7905))
    print(ettskred.wkt())
    print(ettskred.egenskapverdi(2326))
"""