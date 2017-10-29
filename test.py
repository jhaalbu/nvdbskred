import nvdbapi
import pandas as pd

from flask import Flask, request, render_template
from wtforms import Form, IntegerField, StringField, validators
import requests


#print(data)
def hentSkred(veg='Fv241', fylke=14):
    skredtypenr = [4198, 4199, 5351, 4200, 4201, 4202, 4203, 13103]
    skredtype = {4198 : 'Stein', 4199: 'Jord/løsmasse', 5351: 'Is/stein', 4200: 'Snø', 4201: 'Is', 4202: 'Flomskred (vann+stein+jord)', 4203: 'Sørpeskred (vann+snø+stein)', 13103: 'Utglidning av veg'}
    liste = []
    skred = nvdbapi.nvdbFagdata(445)
    skred.addfilter_geo( { 'vegreferanse' : veg, 'fylke' : fylke})
#print(skred.egenskaper())
#skred.addfilter_egenskap('2326=4198')
#stat = skred.statistikk()
#liste.append((skredtype[skredtypenr[0]], stat['antall']))
    sNum = 0
    data = []
    for i in skredtypenr:
        #print(i)
        #print(skredtype[i])
        skred.addfilter_egenskap('2326=' + str(skredtypenr[sNum]))
        stat = skred.statistikk()
        data.append([skredtype[i], stat['antall']])
        sNum = sNum + 1
    return data

def enkeltSkred():
    #a = nvdbapi.nvdbFagdata(445)
    #a.addfilter_geo( { 'vegreferanse' : 'fv241', 'fylke' : 14} )
    #a.addfilter_egenskap('2326=4198')
    ##skredObj.addfilter_egenskap('2326=4198')
    #stat = a.statistikk()
    #print(stat)
    #b = a.nesteNvdbFagObjekt()
    #print(b.egenskaper())

    n = nvdbapi.nvdbFagdata(445)
    n.addfilter_geo( {'vegreferanse' : '1400 fv241  obj = rstat.json()'})
    n.addfilter_egenskap('2326=4198')
    skred = n.nesteForekomst()
    print(skred)
    print(n.statistikk())
    return 'ok'

def enkeltSkredFagObj():
    skredO = nvdbapi.nvdbFagdata(445)
    skredO.addfilter_geo( { 'vegreferanse' : '1400 fv241 hp1'} )
    #skredO.addfilter_egenskap('2326=4198')
    #ettobjekt = skredO.egenskapverdi()

    return ettobjekt

#print(hentSkred())
enkeltSkred()
#print(liste)
#print(skred.statistikk())
#ettskred = skred.nesteNvdbFagObjekt()
#print(ettskred.egenskapverdi(2326))
#print(ettskred.egenskapverdi(2324))
#print(ettskred.egenskap(2326))
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